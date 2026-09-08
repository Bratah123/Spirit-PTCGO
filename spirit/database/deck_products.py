"""Atomic opening of fixed deck products and creation of their saved deck."""

import uuid
from collections import Counter

from sqlalchemy import text

from spirit.database import Collection, Deck, db_session


def open_deck_product(account_id, product, *, purchased=False):
    """Consumes one owned deck, grants its cards, and saves a playable copy."""
    with db_session() as session:
        session.execute(text("BEGIN IMMEDIATE"))
        tradable = True
        if not purchased:
            item = session.get(Collection, (account_id, product.guid))
            if item is None or item.tradable_count + item.nontradable_count <= 0:
                raise ValueError("The account does not own this deck product")
            tradable = item.nontradable_count <= 0
            field = "tradable_count" if tradable else "nontradable_count"
            setattr(item, field, getattr(item, field) - 1)
        contents = product.open(account_id)
        field = "tradable_count" if tradable else "nontradable_count"
        counts = Counter(contents)
        owned = {row.archetype_id: row for row in session.query(Collection).filter(
            Collection.account_id == account_id, Collection.archetype_id.in_(counts))}
        for guid, count in counts.items():
            item = owned.get(guid)
            if item is None:
                item = Collection(account_id=account_id, archetype_id=guid,
                                  tradable_count=0, nontradable_count=0)
                session.add(item)
            setattr(item, field, getattr(item, field) + count)
        deck_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"spirit:deck-product:{account_id}:{product.guid}"))
        if session.get(Deck, deck_id) is None:
            deck = product.to_deck_dict(deck_id)
            session.add(Deck(id=deck_id, account_id=account_id, name=product.name,
                             deck_data=deck, is_avatar=False))
    return contents, tradable
