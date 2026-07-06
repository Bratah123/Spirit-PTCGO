import logging
import random
import string
import uuid

from spirit.database import (
    db_session, Wallet, Collection, Account,
    RedemptionCode, CodeRedemptionEntry, ShopItem, DynamicPage, TradeOffer
)

CODE_ALPHABET = string.ascii_uppercase + string.digits


def _code_to_dict(c):
    return {
        "code_string": c.code_string,
        "reward_json": c.reward_json,
        "max_uses": c.max_uses,
        "current_uses": c.current_uses,
        "enabled": bool(c.enabled),
        "created_at": str(c.created_at)
    }


def _shop_item_to_dict(s):
    return {
        "id": s.id,
        "product_guid": s.product_guid,
        "display_name": s.display_name,
        "currency": s.currency,
        "price": s.price,
        "enabled": bool(s.enabled),
        "featured": bool(s.featured),
        "top_selling": bool(s.top_selling),
        "sort_order": s.sort_order
    }


def _page_to_dict(p):
    return {
        "id": p.id,
        "page_type": p.page_type,
        "sort_order": p.sort_order,
        "content_json": p.content_json,
        "enabled": bool(p.enabled)
    }


def generate_code_string() -> str:
    parts = ["".join(random.choices(CODE_ALPHABET, k=4)) for _ in range(3)]
    return "SPIRIT-" + "-".join(parts)


# ---------------------------------------------------------------- Codes

def list_codes():
    with db_session() as session:
        rows = session.query(RedemptionCode).order_by(RedemptionCode.created_at.desc()).all()
        return [_code_to_dict(r) for r in rows]


def create_code(code_string=None, reward=None, max_uses=1, enabled=True):
    """Creates a redemption code; auto-generates the code string when omitted."""
    reward = reward or {}
    with db_session() as session:
        code_string = (code_string or "").strip().upper() or generate_code_string()
        if session.query(RedemptionCode).filter_by(code_string=code_string).first():
            return None
        code = RedemptionCode(
            code_string=code_string,
            reward_json=reward,
            max_uses=int(max_uses),
            enabled=bool(enabled)
        )
        session.add(code)
        session.flush()
        return _code_to_dict(code)


def update_code(code_string, reward=None, max_uses=None, enabled=None):
    with db_session() as session:
        code = session.query(RedemptionCode).filter_by(code_string=code_string).first()
        if not code:
            return None
        if reward is not None:
            code.reward_json = reward
        if max_uses is not None:
            code.max_uses = int(max_uses)
        if enabled is not None:
            code.enabled = bool(enabled)
        session.flush()
        return _code_to_dict(code)


def delete_code(code_string):
    with db_session() as session:
        entries = session.query(CodeRedemptionEntry).filter_by(code_string=code_string)
        entries.delete(synchronize_session=False)
        deleted = session.query(RedemptionCode).filter_by(code_string=code_string).delete()
        return deleted > 0


def check_code(code_string, account_id):
    """Validates a code for an account. Returns (ok, reward_or_None, reason_token)."""
    with db_session() as session:
        code = session.query(RedemptionCode).filter_by(code_string=code_string.strip().upper()).first()
        if not code or not code.enabled:
            return False, None, "shop.redeemcodes.error.invalidcode"
        if code.max_uses > 0 and code.current_uses >= code.max_uses:
            return False, None, "shop.redeemcodes.error.codeexpired"
        already = session.query(CodeRedemptionEntry).filter_by(
            code_string=code.code_string, account_id=account_id).first()
        if already:
            return False, None, "shop.redeemcodes.error.codealreadyused"
        return True, code.reward_json, None


def redeem_code(code_string, account_id):
    """Atomically redeems a code and grants its rewards. Returns (ok, reward_or_None, reason_token)."""
    code_string = code_string.strip().upper()
    try:
        with db_session() as session:
            code = session.query(RedemptionCode).filter_by(code_string=code_string).first()
            if not code or not code.enabled:
                return False, None, "shop.redeemcodes.error.invalidcode"
            if code.max_uses > 0 and code.current_uses >= code.max_uses:
                return False, None, "shop.redeemcodes.error.codeexpired"
            already = session.query(CodeRedemptionEntry).filter_by(
                code_string=code_string, account_id=account_id).first()
            if already:
                return False, None, "shop.redeemcodes.error.codealreadyused"

            code.current_uses += 1
            session.add(CodeRedemptionEntry(code_string=code_string, account_id=account_id))

            reward = code.reward_json or {}
            _grant_reward_in_session(session, account_id, reward)
            return True, reward, None
    except Exception as e:
        logging.error(f"[Economy] Failed to redeem code {code_string} for {account_id}: {e}")
        return False, None, "shop.redeemcodes.error.invalidcode"


def _grant_reward_in_session(session, account_id, reward):
    """Applies a reward dict to an account inside an open session."""
    for guid, count in (reward.get("products") or {}).items():
        item = session.query(Collection).filter_by(
            account_id=account_id, archetype_id=guid).first()
        if item:
            item.nontradable_count += int(count)
        else:
            session.add(Collection(
                account_id=account_id, archetype_id=guid,
                tradable_count=0, nontradable_count=int(count)))

    coins = int(reward.get("coins") or 0)
    gems = int(reward.get("gems") or 0)
    tickets = int(reward.get("tickets") or 0)
    if coins or gems or tickets:
        wallet = session.query(Wallet).filter_by(account_id=account_id).first()
        if not wallet:
            wallet = Wallet(account_id=account_id, coins=0, gems=0, tickets=0)
            session.add(wallet)
        wallet.coins += coins
        wallet.gems += gems
        wallet.tickets += tickets


# ---------------------------------------------------------------- Shop items

def list_shop_items(enabled_only=False):
    with db_session() as session:
        q = session.query(ShopItem)
        if enabled_only:
            q = q.filter_by(enabled=True)
        rows = q.order_by(ShopItem.sort_order, ShopItem.id).all()
        return [_shop_item_to_dict(r) for r in rows]


def upsert_shop_item(product_guid, display_name=None, currency=None, price=None,
                     enabled=None, featured=None, top_selling=None, sort_order=None, item_id=None):
    """Creates or updates a shop item (matched by id, then product_guid)."""
    with db_session() as session:
        item = None
        if item_id is not None:
            item = session.query(ShopItem).filter_by(id=int(item_id)).first()
        if item is None:
            item = session.query(ShopItem).filter_by(product_guid=product_guid).first()
        if item is None:
            item = ShopItem(product_guid=product_guid)
            session.add(item)
        else:
            item.product_guid = product_guid

        if display_name is not None:
            item.display_name = display_name
        if currency is not None:
            item.currency = int(currency)
        if price is not None:
            item.price = int(price)
        if enabled is not None:
            item.enabled = bool(enabled)
        if featured is not None:
            item.featured = bool(featured)
        if top_selling is not None:
            item.top_selling = bool(top_selling)
        if sort_order is not None:
            item.sort_order = int(sort_order)
        session.flush()
        return _shop_item_to_dict(item)


def delete_shop_item(item_id):
    with db_session() as session:
        deleted = session.query(ShopItem).filter_by(id=int(item_id)).delete()
        return deleted > 0


# ---------------------------------------------------------------- Dynamic pages

def list_dynamic_pages(enabled_only=False, page_type=None):
    with db_session() as session:
        q = session.query(DynamicPage)
        if enabled_only:
            q = q.filter_by(enabled=True)
        if page_type:
            q = q.filter_by(page_type=page_type)
        rows = q.order_by(DynamicPage.sort_order, DynamicPage.id).all()
        return [_page_to_dict(r) for r in rows]


def upsert_dynamic_page(content_json, page_id=None, page_type="landing", sort_order=0, enabled=True):
    with db_session() as session:
        page = None
        if page_id is not None:
            page = session.query(DynamicPage).filter_by(id=int(page_id)).first()
        if page is None:
            page = DynamicPage(content_json=content_json)
            session.add(page)
        page.content_json = content_json
        page.page_type = page_type
        page.sort_order = int(sort_order)
        page.enabled = bool(enabled)
        session.flush()
        return _page_to_dict(page)


def delete_dynamic_page(page_id):
    with db_session() as session:
        deleted = session.query(DynamicPage).filter_by(id=int(page_id)).delete()
        return deleted > 0


# ---------------------------------------------------------------- Trade offers

def _offer_to_dict(t, screen_names=None):
    screen_names = screen_names or {}
    return {
        "id": t.id,
        "offer_id": t.offer_id,
        "sender_id": t.sender_id,
        "sender_name": screen_names.get(t.sender_id, ""),
        "recipient_id": t.recipient_id,
        "offering": t.offering_json,
        "requesting": t.requesting_json,
        "status": t.status,
        "accepted_by": t.accepted_by,
        "created_at": str(t.created_at)
    }


def _screen_names_for(session, account_ids):
    if not account_ids:
        return {}
    rows = session.query(Account).filter(Account.account_id.in_(list(account_ids))).all()
    return {a.account_id: (a.screen_name or a.username) for a in rows}


def _has_tradable(session, account_id, wanted):
    """Checks the account owns every {guid: count} in wanted as tradable copies."""
    for guid, count in wanted.items():
        item = session.query(Collection).filter_by(
            account_id=account_id, archetype_id=guid).first()
        if not item or item.tradable_count < int(count):
            return False, guid
    return True, None


def _transfer(session, from_id, to_id, items):
    """Moves {guid: count} tradable copies between two collections inside an open session."""
    for guid, count in items.items():
        count = int(count)
        src = session.query(Collection).filter_by(
            account_id=from_id, archetype_id=guid).first()
        src.tradable_count -= count
        dst = session.query(Collection).filter_by(
            account_id=to_id, archetype_id=guid).first()
        if dst:
            dst.tradable_count += count
        else:
            session.add(Collection(account_id=to_id, archetype_id=guid,
                                   tradable_count=count, nontradable_count=0))


def create_trade_offer(sender_id, offering, requesting, recipient_id=None):
    """Creates a trade offer after verifying the sender owns the offered items.

    Returns (offer_dict_or_None, error_key_or_None)."""
    offering = {k: int(v) for k, v in (offering or {}).items() if int(v) > 0}
    requesting = {k: int(v) for k, v in (requesting or {}).items() if int(v) > 0}
    if not offering or not requesting:
        return None, "trade.errorCreatingLotDialog.body"

    with db_session() as session:
        ok, _missing = _has_tradable(session, sender_id, offering)
        if not ok:
            return None, "trade.createLot.notEnoughCards.body"
        offer = TradeOffer(
            offer_id=str(uuid.uuid4()),
            sender_id=sender_id,
            recipient_id=recipient_id,
            offering_json=offering,
            requesting_json=requesting,
            status="open"
        )
        session.add(offer)
        session.flush()
        return _offer_to_dict(offer), None


def _trade_offer_query(session, public=None, sender_id=None, recipient_id=None,
                       exclude_sender_id=None, status="open"):
    q = session.query(TradeOffer)
    if status:
        q = q.filter_by(status=status)
    if public is True:
        q = q.filter(TradeOffer.recipient_id.is_(None))
    if sender_id:
        q = q.filter_by(sender_id=sender_id)
    if recipient_id:
        q = q.filter_by(recipient_id=recipient_id)
    if exclude_sender_id:
        q = q.filter(TradeOffer.sender_id != exclude_sender_id)
    return q


def list_trade_offers(public=None, sender_id=None, recipient_id=None,
                      exclude_sender_id=None, status="open", offset=0, limit=50):
    """Returns (offers, total_count) filtered by visibility."""
    with db_session() as session:
        q = _trade_offer_query(session, public, sender_id, recipient_id,
                               exclude_sender_id, status)
        total = q.count()
        rows = q.order_by(TradeOffer.created_at.desc()).offset(int(offset)).limit(int(limit)).all()
        names = _screen_names_for(session, {r.sender_id for r in rows})
        return [_offer_to_dict(r, names) for r in rows], total


def count_trade_offers(public=None, sender_id=None, recipient_id=None,
                       exclude_sender_id=None, status="open"):
    """Lightweight count matching list_trade_offers' filters (no serialization)."""
    with db_session() as session:
        return _trade_offer_query(session, public, sender_id, recipient_id,
                                  exclude_sender_id, status).count()


def get_trade_offer(offer_id):
    with db_session() as session:
        offer = session.query(TradeOffer).filter_by(offer_id=offer_id).first()
        if not offer:
            return None
        names = _screen_names_for(session, {offer.sender_id})
        return _offer_to_dict(offer, names)


def cancel_trade_offer(offer_id, account_id):
    """Cancels an open offer; only the sender (or its private recipient rejecting) may do so."""
    with db_session() as session:
        offer = session.query(TradeOffer).filter_by(offer_id=offer_id, status="open").first()
        if not offer:
            return False
        if offer.sender_id != account_id and offer.recipient_id != account_id:
            return False
        offer.status = "cancelled" if offer.sender_id == account_id else "declined"
        return True


def accept_trade_offer(offer_id, accepter_id):
    """Atomically swaps the traded items between the two accounts.

    Returns (offer_dict_or_None, error_key_or_None). The whole swap runs in a
    single transaction: any failed precondition rolls everything back."""
    try:
        with db_session() as session:
            offer = session.query(TradeOffer).filter_by(offer_id=offer_id, status="open").first()
            if not offer:
                return None, "trade.errorPurchasingLotDialog.bodyFormat"
            if offer.sender_id == accepter_id:
                return None, "trade.errorPurchasingLotDialog.bodyFormat"
            if offer.recipient_id and offer.recipient_id != accepter_id:
                return None, "trade.errorPurchasingLotDialog.bodyFormat"

            # The sender must still own what they offered
            ok, _ = _has_tradable(session, offer.sender_id, offer.offering_json)
            if not ok:
                offer.status = "cancelled"
                return None, "trade.errorPurchasingLotDialog.bodyFormat"

            # The accepter must own what the sender requested
            ok, _ = _has_tradable(session, accepter_id, offer.requesting_json)
            if not ok:
                return None, "trade.createLot.notEnoughCards.body"

            _transfer(session, offer.sender_id, accepter_id, offer.offering_json)
            _transfer(session, accepter_id, offer.sender_id, offer.requesting_json)

            offer.status = "accepted"
            offer.accepted_by = accepter_id
            session.flush()
            return _offer_to_dict(offer), None
    except Exception as e:
        logging.error(f"[Economy] Trade accept failed for {offer_id}: {e}", exc_info=True)
        return None, "trade.errorPurchasingLotDialog.bodyFormat"
