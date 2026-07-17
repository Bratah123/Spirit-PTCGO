import base64
import binascii
import json
import logging
import os
import re

from urllib.parse import unquote
from spirit.server import http_server
from spirit.database import db_session, Account, TradeOffer
from spirit.database import economy_data
from spirit.game import season_manager
from spirit.game.attributes import AttrID
from spirit.game.models.versus import VersusSeason
from spirit.game.set_utils import card_script_counts, eligible_booster_sets
from spirit.server import admin_auth
from spirit.server import dynamic_pages
from spirit.server import metrics

DASHBOARD_PATH = os.path.join(os.path.dirname(__file__), 'admin', 'dashboard.html')
CARDS_IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'cards')

_CARD_IMAGE_INDEX = None


def _json(status, payload):
    return status, json.dumps(payload).encode('utf-8'), 'application/json'


def _ok(payload=None):
    return _json(200, {"ok": True, **(payload or {})})


def _err(status, message):
    return _json(status, {"ok": False, "error": message})


def _decode_image_data_url(value):
    if not isinstance(value, str):
        raise ValueError("image data is required")
    header, separator, encoded = value.partition(',')
    allowed = {
        'data:image/png;base64',
        'data:image/jpeg;base64',
        'data:image/jpg;base64',
        'data:image/webp;base64',
    }
    if separator != ',' or header.lower() not in allowed:
        raise ValueError("upload a PNG, JPEG, or WebP image")
    max_encoded = ((dynamic_pages.MAX_CUSTOM_IMAGE_BYTES + 2) // 3) * 4
    if len(encoded) > max_encoded:
        raise ValueError("custom artwork must be 12 MB or smaller")
    try:
        return base64.b64decode(encoded, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise ValueError("image upload is not valid base64 data") from exc


def _products_summary():
    from spirit.game.scripts.products import loader as product_loader
    if not product_loader.products:
        product_loader.load_all()
    out = []
    for p in product_loader.products:
        out.append({
            "guid": p.guid,
            "key": p.key,
            "name": p.name,
            "product_type": p.product_type,
            "image": p.get_attribute_value(AttrID.IMAGE_NAME, "")
        })
    return out


def _card_image_index():
    """{(set_dir, collector_number): filename} from assets/cards/<SET>/Name_<num>.png."""
    global _CARD_IMAGE_INDEX
    if _CARD_IMAGE_INDEX is not None:
        return _CARD_IMAGE_INDEX
    index = {}
    if os.path.isdir(CARDS_IMG_DIR):
        for set_dir in os.listdir(CARDS_IMG_DIR):
            full = os.path.join(CARDS_IMG_DIR, set_dir)
            if not os.path.isdir(full):
                continue
            for f in os.listdir(full):
                stem, ext = os.path.splitext(f)
                if ext.lower() != '.png' or stem.endswith(('_foil', '_energypip', '_toolpip')):
                    continue
                num = stem.rsplit('_', 1)[-1]
                if num.isdigit():
                    index.setdefault((set_dir, int(num)), f)
    _CARD_IMAGE_INDEX = index
    return index


def _card_image_url(set_key, collector_number):
    try:
        num = int(collector_number)
    except (TypeError, ValueError):
        return None
    if (set_key, num) in _card_image_index():
        return f"/admin/api/card-image/{set_key}/{num}"
    return None


def _validate_seasons(seasons):
    """Round-trips season dicts through the model. Returns (normalized, error)."""
    if not isinstance(seasons, list) or not seasons:
        return None, "seasons must be a non-empty list"
    normalized = []
    for i, raw in enumerate(seasons):
        if not isinstance(raw, dict) or not str(raw.get("seasonID") or "").strip():
            return None, f"season {i}: seasonID required"
        season = VersusSeason.from_dict(raw)
        for tier in season.tiers:
            for points, rewards in tier.rewards.items():
                if points <= 0:
                    return None, f"season {i}: tier thresholds must be positive"
                for r in rewards:
                    if not r.reward_type:
                        return None, f"season {i}: reward missing rewardType"
                    if r.reward_type == "Archetype" and not r.reward_product_id:
                        return None, f"season {i}: Archetype reward missing rewardProductID"
                # client dereferences reward[0]'s archetype unguarded when a
                # milestone has 2+ rewards — one must be a card/product
                if len(rewards) >= 2 and not any(
                        (r.reward_product_id or "").strip("0-") for r in rewards):
                    return None, (f"season {i}: milestone {points} has multiple rewards "
                                  "but no card/product — the client requires the first "
                                  "reward of a multi-reward milestone to be an archetype")
        normalized.append(season.to_dict())
    return normalized, None


def _accounts_summary():
    with db_session() as session:
        rows = session.query(Account).all()
        return [{"account_id": a.account_id, "username": a.username,
                 "screen_name": a.screen_name, "is_admin": bool(a.is_admin)} for a in rows]


def _tournament_entry_counts(tournament_ids):
    from sqlalchemy import func
    from spirit.database import TournamentEntry
    if not tournament_ids:
        return {}
    with db_session() as session:
        rows = (session.query(TournamentEntry.tournament_id, func.count())
                .filter(TournamentEntry.tournament_id.in_(tournament_ids))
                .group_by(TournamentEntry.tournament_id).all())
        return dict(rows)


def _trades_summary():
    with db_session() as session:
        rows = session.query(TradeOffer).order_by(TradeOffer.created_at.desc()).limit(100).all()
        return [{
            "offer_id": t.offer_id, "sender_id": t.sender_id,
            "recipient_id": t.recipient_id, "status": t.status,
            "offering": t.offering_json, "requesting": t.requesting_json,
            "accepted_by": t.accepted_by, "created_at": str(t.created_at)
        } for t in rows]


def _reload_shop():
    try:
        from spirit.shop import shop_manager
        shop_manager.reload_from_db()
    except Exception as e:
        logging.error(f"[Admin] Shop reload failed: {e}")


def _login(data):
    from spirit.database.admin_data import verify_admin_login
    admin = verify_admin_login(data.get("username", ""), data.get("password", ""))
    if not admin:
        return _err(401, "invalid credentials or not an admin account")
    token = admin_auth.create_session(admin["account_id"], admin["username"])
    status, payload, ctype = _ok({"username": admin["username"]})
    return status, payload, ctype, [("Set-Cookie", admin_auth.session_cookie(token))]


def route_admin(method, path, body, headers=None):
    """Routes an /admin request.

    Returns (status, payload_bytes, content_type) or a 4-tuple with an extra
    [(header, value)] list (Set-Cookie on login/logout)."""
    path = path.rstrip('/') or '/admin'

    # The dashboard HTML is public — it gates itself behind /admin/api/session.
    if method == 'GET' and path == '/admin':
        try:
            with open(DASHBOARD_PATH, 'rb') as f:
                return 200, f.read(), 'text/html; charset=utf-8'
        except OSError:
            return _err(500, "dashboard.html missing")

    if not path.startswith('/admin/api/'):
        return _err(404, "unknown admin route")

    endpoint = path[len('/admin/api/'):]
    data = {}
    if body:
        try:
            data = json.loads(body)
        except (json.JSONDecodeError, TypeError):
            return _err(400, "invalid JSON body")

    token = admin_auth.token_from_headers(headers)
    session = admin_auth.get_session(token)

    if method == 'POST' and endpoint == 'login':
        return _login(data)
    if method == 'POST' and endpoint == 'logout':
        admin_auth.destroy_session(token)
        status, payload, ctype = _ok()
        return status, payload, ctype, [("Set-Cookie", admin_auth.session_cookie("", clear=True))]
    if method == 'GET' and endpoint == 'session':
        if session:
            return _ok({"authenticated": True, "username": session["username"]})
        return _json(200, {"ok": True, "authenticated": False})

    if session is None:
        return _err(401, "authentication required")

    try:
        return _dispatch(method, endpoint, data)
    except Exception as e:
        logging.error(f"[Admin] API error on {method} {path}: {e}", exc_info=True)
        return _err(500, str(e))


def _dispatch(method, endpoint, data):
    # ------------------------------------------------ metrics (ops observability)
    if method == 'GET' and endpoint == 'metrics':
        return _json(200, metrics.snapshot())

    # ------------------------------------------------ overview / reference data
    if method == 'GET' and endpoint == 'overview':
        return _ok({
            "accounts": len(_accounts_summary()),
            "codes": len(economy_data.list_codes()),
            "shop_items": len(economy_data.list_shop_items()),
            "pages": len(economy_data.list_dynamic_pages()),
            "trades": len(_trades_summary()),
            "eligible_sets": eligible_booster_sets(),
            "set_counts": card_script_counts()
        })

    if method == 'GET' and endpoint == 'products':
        return _ok({"products": _products_summary()})

    if method == 'GET' and endpoint == 'accounts':
        return _ok({"accounts": _accounts_summary()})

    if method == 'POST' and endpoint == 'accounts/grant-all-cards':
        account_id = data.get("account_id")
        if not account_id:
            return _err(400, "account_id required")
        with db_session() as session:
            if not session.query(Account).filter_by(account_id=account_id).first():
                return _err(404, "account not found")
        from spirit.database.player_data import grant_all_cards
        count = max(1, int(data.get("count") or 4))
        granted = grant_all_cards(account_id, count=count, is_tradable=True)
        return _ok({"granted": granted, "count": count})

    if method == 'POST' and endpoint == 'accounts/grant-all-products':
        account_id = data.get("account_id")
        if not account_id:
            return _err(400, "account_id required")
        with db_session() as session:
            if not session.query(Account).filter_by(account_id=account_id).first():
                return _err(404, "account not found")
        from spirit.database.player_data import grant_all_products
        count = max(1, int(data.get("count") or 1))
        granted = grant_all_products(account_id, count=count, is_tradable=True)
        return _ok({"granted": granted, "count": count})

    if method == 'POST' and endpoint == 'accounts/set-admin':
        from spirit.database.admin_data import set_admin
        account_id = data.get("account_id")
        if not account_id:
            return _err(400, "account_id required")
        if not set_admin(account_id, bool(data.get("is_admin"))):
            return _err(404, "account not found")
        return _ok({"account_id": account_id, "is_admin": bool(data.get("is_admin"))})

    if method == 'GET' and endpoint == 'trades':
        return _ok({"trades": _trades_summary()})

    if method == 'GET' and endpoint == 'cards/search':
        return _err(400, "use POST with {query}")

    if method == 'POST' and endpoint == 'cards/search':
        from spirit.game.scripts.cards import loader as card_loader
        if not card_loader.cards:
            card_loader.load_all()
        query = (data.get("query") or "").lower()
        set_filter = (data.get("set") or "").upper()
        results = []
        if query or set_filter:
            for c in card_loader.cards:
                if set_filter and c.key.upper() != set_filter:
                    continue
                name = (c.display_name or "")
                haystack = f"{name} {c.guid} {c.key}".lower()
                if query and query not in haystack:
                    continue
                number = c.get_attribute_value(AttrID.COLLECTOR_NUMBER)
                results.append({
                    "guid": c.guid, "name": name, "set": c.key, "number": number,
                    "rarity": getattr(c, "rarity", None),
                    "image": _card_image_url(c.key, number)
                })
                if len(results) >= 60:
                    break
        return _ok({"cards": results})

    if method == 'POST' and endpoint == 'cards/lookup':
        from spirit.game.scripts.cards import loader as card_loader
        if not card_loader.cards:
            card_loader.load_all()
        wanted = {str(g).lower() for g in (data.get("guids") or [])}
        results = {}
        for c in card_loader.cards:
            if c.guid.lower() in wanted:
                number = c.get_attribute_value(AttrID.COLLECTOR_NUMBER)
                results[c.guid.lower()] = {
                    "guid": c.guid, "name": c.display_name or "", "set": c.key,
                    "number": number, "image": _card_image_url(c.key, number)
                }
        return _ok({"cards": results})

    if method == 'GET' and endpoint.startswith('card-image/'):
        parts = endpoint.split('/')
        if len(parts) != 3 or not re.fullmatch(r'[A-Za-z0-9_-]+', parts[1]) or not parts[2].isdigit():
            return _err(400, "card-image/<set>/<number>")
        filename = _card_image_index().get((parts[1], int(parts[2])))
        if not filename:
            return _err(404, "card image not found")
        with open(os.path.join(CARDS_IMG_DIR, parts[1], filename), 'rb') as f:
            return 200, f.read(), 'image/png'

    # ------------------------------------------------ versus seasons
    if endpoint == 'versus-seasons':
        if method == 'GET':
            try:
                with open(season_manager.SEASONS_PATH, 'r', encoding='utf-8') as f:
                    seasons = json.load(f)
            except (OSError, json.JSONDecodeError):
                seasons = []
            return _ok({"seasons": seasons})
        if method == 'POST':
            normalized, error = _validate_seasons(data.get("seasons"))
            if error:
                return _err(400, error)
            with open(season_manager.SEASONS_PATH, 'w', encoding='utf-8') as f:
                json.dump(normalized, f, indent=2)
            season_manager.VersusSeasonManager().load_seasons()
            return _ok({"seasons": normalized})

    # ------------------------------------------------ play formats
    if endpoint == 'formats':
        from spirit.game import format_manager
        if method == 'GET':
            mgr = format_manager.FormatManager()
            return _ok({
                "formats": [fmt.to_dict() for fmt in mgr.formats],
                "sets": sorted(card_script_counts().keys())
            })
        if method == 'POST':
            normalized, error = format_manager.validate_formats(data.get("formats"))
            if error:
                return _err(400, error)
            with open(format_manager.FORMATS_PATH, 'w', encoding='utf-8') as f:
                json.dump({"formats": normalized}, f, indent=2)
            format_manager.FormatManager().load_formats()
            # Re-derive set legalFormats and drop cached format-legality payloads
            from spirit.packets.handlers import data_sync
            data_sync.reload_sets()
            return _ok({"formats": normalized})

    # ------------------------------------------------ async tournaments
    if endpoint == 'tournaments':
        from spirit.database import tournament_data
        from spirit.game.tournament_manager import TournamentManager, validate_definition
        if method == 'GET':
            tournaments = tournament_data.list_tournaments()
            counts = _tournament_entry_counts([t["tournament_id"] for t in tournaments])
            for t in tournaments:
                t["entries"] = counts.get(t["tournament_id"], 0)
            return _ok({"tournaments": tournaments})
        if method == 'POST':
            error = validate_definition(data.get("definition"))
            if error:
                return _err(400, error)
            saved = tournament_data.upsert_tournament(
                definition=data["definition"],
                tournament_id=data.get("tournament_id"),
                enabled=data.get("enabled"))
            TournamentManager().reload_from_db()
            return _ok({"tournament": saved})

    if method == 'POST' and endpoint == 'tournaments/toggle':
        from spirit.database import tournament_data
        from spirit.game.tournament_manager import TournamentManager
        rows = {t["tournament_id"]: t for t in tournament_data.list_tournaments()}
        row = rows.get(data.get("tournament_id", ""))
        if not row:
            return _err(404, "tournament not found")
        saved = tournament_data.upsert_tournament(
            definition=None, tournament_id=row["tournament_id"],
            enabled=not row["enabled"])
        TournamentManager().reload_from_db()
        return _ok({"tournament": saved})

    if method == 'POST' and endpoint == 'tournaments/delete':
        from spirit.database import tournament_data
        from spirit.game.tournament_manager import TournamentManager
        if not tournament_data.delete_tournament(data.get("tournament_id", "")):
            return _err(404, "tournament not found")
        TournamentManager().reload_from_db()
        return _ok()

    if method == 'GET' and endpoint.startswith('tournaments/standings/'):
        from spirit.database import tournament_data
        from spirit.game.tournament_manager import TournamentManager
        tournament_id = endpoint.split('/', 2)[2]
        tournament = TournamentManager().get(tournament_id)
        definition = tournament.definition if tournament else {}
        return _ok({"standings": tournament_data.leaderboard_standings(
            tournament_id, definition)})

    # ------------------------------------------------ redemption codes
    if endpoint == 'codes':
        if method == 'GET':
            return _ok({"codes": economy_data.list_codes()})
        if method == 'POST':
            created = []
            count = max(1, int(data.get("count") or 1))
            for _ in range(count):
                code = economy_data.create_code(
                    code_string=data.get("code") if count == 1 else None,
                    reward=data.get("reward") or {},
                    max_uses=data.get("max_uses", 1),
                    enabled=data.get("enabled", True)
                )
                if code is None:
                    return _err(409, "code already exists")
                created.append(code)
            return _ok({"codes": created})

    if method == 'POST' and endpoint == 'codes/update':
        code = economy_data.update_code(
            data.get("code", ""),
            reward=data.get("reward"),
            max_uses=data.get("max_uses"),
            enabled=data.get("enabled")
        )
        if code is None:
            return _err(404, "code not found")
        return _ok({"code": code})

    if method == 'POST' and endpoint == 'codes/delete':
        if not economy_data.delete_code(data.get("code", "")):
            return _err(404, "code not found")
        return _ok()

    # ------------------------------------------------ shop items
    if endpoint == 'shop':
        if method == 'GET':
            return _ok({
                "items": economy_data.list_shop_items(),
                "eligible_sets": eligible_booster_sets()
            })
        if method == 'POST':
            if not data.get("product_guid"):
                return _err(400, "product_guid required")
            item = economy_data.upsert_shop_item(
                product_guid=data["product_guid"],
                display_name=data.get("display_name"),
                currency=data.get("currency"),
                price=data.get("price"),
                enabled=data.get("enabled"),
                featured=data.get("featured"),
                top_selling=data.get("top_selling"),
                sort_order=data.get("sort_order"),
                item_id=data.get("id")
            )
            _reload_shop()
            return _ok({"item": item})

    if method == 'POST' and endpoint == 'shop/toggle':
        items = {i["id"]: i for i in economy_data.list_shop_items()}
        item = items.get(int(data.get("id", -1)))
        if not item:
            return _err(404, "shop item not found")
        updated = economy_data.upsert_shop_item(
            product_guid=item["product_guid"],
            enabled=not item["enabled"],
            item_id=item["id"]
        )
        _reload_shop()
        return _ok({"item": updated})

    if method == 'POST' and endpoint == 'shop/delete':
        if not economy_data.delete_shop_item(data.get("id", -1)):
            return _err(404, "shop item not found")
        _reload_shop()
        return _ok()

    # ------------------------------------------------ dynamic pages
    if method == 'GET' and endpoint == 'pages/assets':
        return _ok(dynamic_pages.asset_catalog_payload())

    if method == 'POST' and endpoint == 'pages/assets/refresh':
        dynamic_pages.invalidate_asset_catalog()
        try:
            build = dynamic_pages.compile_custom_landing_bundle(force=True)
        except dynamic_pages.PageValidationError as exc:
            return _err(400, str(exc))
        dynamic_pages.invalidate_asset_catalog()
        if build.get("built"):
            http_server.register_asset_path(dynamic_pages.BUNDLE_CACHE_DIR)
        return _ok({**dynamic_pages.asset_catalog_payload(), "custom_build": build})

    if method == 'POST' and endpoint == 'pages/assets/custom':
        try:
            image_bytes = _decode_image_data_url(data.get("image"))
            imported = dynamic_pages.save_custom_landing_image(
                data.get("name", ""),
                image_bytes,
                replace=bool(data.get("replace", False)),
            )
        except (ValueError, dynamic_pages.PageValidationError) as exc:
            return _err(400, str(exc))

        from spirit.server import http_server
        http_server.register_asset_path(dynamic_pages.BUNDLE_CACHE_DIR)
        catalog = dynamic_pages.asset_catalog_payload()
        imported["catalog_asset"] = next(
            (
                asset
                for asset in catalog["assets"]
                if asset["name"].casefold() == imported["name"].casefold()
            ),
            None,
        )
        return _ok({"asset": imported, **catalog})

    if method == 'GET' and endpoint.startswith('pages/assets/thumb/'):
        asset_name = unquote(endpoint[len('pages/assets/thumb/'):])
        payload = dynamic_pages.render_asset_jpeg(asset_name, 'thumb')
        if payload is None:
            return _err(404, "landing-page asset not found")
        return 200, payload, 'image/jpeg', [('Cache-Control', 'private, max-age=3600')]

    if method == 'GET' and endpoint.startswith('pages/assets/preview/'):
        asset_name = unquote(endpoint[len('pages/assets/preview/'):])
        payload = dynamic_pages.render_asset_jpeg(asset_name, 'preview')
        if payload is None:
            return _err(404, "landing-page asset not found")
        return 200, payload, 'image/jpeg', [('Cache-Control', 'private, max-age=3600')]

    if endpoint == 'pages':
        if method == 'GET':
            return _ok({"pages": economy_data.list_dynamic_pages()})
        if method == 'POST':
            if not isinstance(data.get("content_json"), dict):
                return _err(400, "content_json object required")
            page_type = data.get("page_type", "landing")
            try:
                content = dynamic_pages.normalize_page(
                    data["content_json"], page_type, data.get("sort_order", 0)
                )
            except dynamic_pages.PageValidationError as exc:
                return _err(400, str(exc))

            installed, unresolved = dynamic_pages.install_page_assets(content)
            if installed:
                # The selected source bundle is now in externalCache.  Publish
                # its LandingPage/<texture> keys immediately so clients can
                # load the same artwork shown by the dashboard preview.
                from spirit.server import http_server
                http_server.register_asset_path(dynamic_pages.EXTERNAL_CACHE_DIR)
            page = economy_data.upsert_dynamic_page(
                content_json=content,
                page_id=data.get("id"),
                page_type=page_type,
                sort_order=content["sortOrder"],
                enabled=data.get("enabled", True)
            )
            return _ok({
                "page": page,
                "installed_bundles": installed,
                "unresolved_assets": unresolved,
            })

    if method == 'POST' and endpoint == 'pages/toggle':
        try:
            page_id = int(data.get("id", -1))
        except (TypeError, ValueError):
            return _err(400, "valid page id required")
        page = next(
            (p for p in economy_data.list_dynamic_pages() if p["id"] == page_id),
            None,
        )
        if page is None:
            return _err(404, "page not found")
        updated = economy_data.upsert_dynamic_page(
            content_json=page["content_json"],
            page_id=page_id,
            page_type=page["page_type"],
            sort_order=page["sort_order"],
            enabled=not page["enabled"],
        )
        return _ok({"page": updated})

    if method == 'POST' and endpoint == 'pages/delete':
        if not economy_data.delete_dynamic_page(data.get("id", -1)):
            return _err(404, "page not found")
        return _ok()

    return _err(404, f"unknown endpoint: {endpoint}")
