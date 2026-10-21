import logging
from spirit.database.connection import db_session
from spirit.database import Base, Account
from sqlalchemy import text

def grant_all_cards_startup():
    try:
        logging.info("[CUSTOM] Starting official native GUID card synchronization...")
        
        cards = []
        try:
            from spirit.game.scripts.cards import loader as card_loader
            cards = card_loader.load_all()
        except Exception as loader_err:
            logging.error(f"[CUSTOM] Native card loader could not be imported: {loader_err}")
            return

        if not cards:
            logging.warning("[CUSTOM] No cards were compiled by the native loader.")
            return

        CollectionModel = None
        for mapper in Base.registry.mappers:
            cls = mapper.class_
            if hasattr(cls, "__tablename__") and cls.__tablename__ == "collection":
                CollectionModel = cls
                break

        if not CollectionModel:
            logging.error("[CUSTOM] Could not find the native Collection model mapping.")
            return

        with db_session() as session:
            # SANITARY CLEAN-UP: Purge malformed/raw database text IDs from previous attempts
            # that cause the client deserialization exceptions to prevent crashes.
            try:
                session.execute(text("DELETE FROM collection WHERE length(archetype_id) != 36"))
                session.commit()
            except Exception as clean_err:
                logging.warning(f"[CUSTOM] Non-critical clean up warning: {clean_err}")

            all_accounts = session.query(Account).all()
            if not all_accounts:
                return

            logging.info(f"[CUSTOM] Found {len(cards)} valid card GUIDs from server scripts.")
            
            for acc in all_accounts:
                logging.info(f"[CUSTOM] Ensuring at least 4 tradable copies of all cards for user: {acc.username}")
                
                # Fetch existing collection into memory to optimize performance and prevent timeouts
                existing_items = {col.archetype_id: col for col in session.query(CollectionModel).filter_by(account_id=acc.account_id).all()}
                
                for card in cards:
                    if hasattr(card, 'guid') and card.guid:
                        guid = card.guid
                        
                        if guid in existing_items:
                            current_item = existing_items[guid]
                            current_tradable = getattr(current_item, 'tradable_count', 0) or 0
                            
                            # RULES APPLIED:
                            # 1. Guaranteed at least 4 copies if current inventory is below 4.
                            # 2. Left untouched if the quantity is already equal to or greater than 4.
                            # 3. No existing nontradable card counts are modified or touched.
                            if current_tradable < 4:
                                current_item.tradable_count = 4
                        else:
                            # Create a fresh database entry if the card doesn't exist yet
                            new_col = CollectionModel(
                                account_id=acc.account_id,
                                archetype_id=guid,
                                tradable_count=4,
                                nontradable_count=0
                            )
                            session.add(new_col)
                            existing_items[guid] = new_col

            session.commit()
            logging.info("[CUSTOM] Success! Legitimate card inventory updated accurately without client crashes.")
                
    except Exception as e:
        logging.error(f"[CUSTOM] Error executing native GUID module: {e}")
