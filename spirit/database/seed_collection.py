import os
import sys
import logging

# Ensure Python can find the 'spirit' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from spirit.database import db_session, Account, Collection
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.scripts.products import loader as product_loader

def seed_collection():
    try:
        # 1. Load all cards from scripts
        cards = card_loader.load_all()
        print(f"Loaded {len(cards)} cards from scripts.")

        # 2. Load all products from scripts
        products = product_loader.load_all()
        print(f"Loaded {len(products)} products from scripts.")

        with db_session() as session:
            # 3. Get all accounts
            accounts = session.query(Account).all()
            print(f"Seeding collection for {len(accounts)} accounts...")
            
            for acc in accounts:
                account_id = acc.account_id
                print(f" - Processing account: {account_id}")
                
                # Pre-fetch existing collection for this account to optimize performance
                existing_items = {col.archetype_id: col for col in session.query(Collection).filter_by(account_id=account_id).all()}
                
                # Add Cards (4x)
                for card in cards:
                    guid = card.guid
                    if guid in existing_items:
                        col_item = existing_items[guid]
                        col_item.tradable_count = max(4, col_item.tradable_count)
                    else:
                        new_col = Collection(
                            account_id=account_id,
                            archetype_id=guid,
                            tradable_count=4,
                            nontradable_count=0
                        )
                        session.add(new_col)
                        existing_items[guid] = new_col
                        
                # Add Products (1x tradable, 1x nontradable)
                for prod in products:
                    guid = prod.guid
                    if guid in existing_items:
                        col_item = existing_items[guid]
                        col_item.tradable_count = max(1, col_item.tradable_count)
                        col_item.nontradable_count = max(1, col_item.nontradable_count)
                    else:
                        new_col = Collection(
                            account_id=account_id,
                            archetype_id=guid,
                            tradable_count=1,
                            nontradable_count=1
                        )
                        session.add(new_col)
                        existing_items[guid] = new_col
                        
                # Add Currencies
                for i in [2, 3]:
                    guid = f"00000000-0000-0000-0000-00000000000{i}"
                    if guid in existing_items:
                        col_item = existing_items[guid]
                        col_item.tradable_count = max(1000, col_item.tradable_count)
                    else:
                        new_col = Collection(
                            account_id=account_id,
                            archetype_id=guid,
                            tradable_count=1000,
                            nontradable_count=0
                        )
                        session.add(new_col)
                        existing_items[guid] = new_col
                        
        print("Database seeding complete!")
        
    except Exception as e:
        print(f"Error seeding collection: {e}")

if __name__ == '__main__':
    seed_collection()
