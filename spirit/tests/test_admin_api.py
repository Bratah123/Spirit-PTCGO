import json
import unittest
import os
import tempfile
from unittest.mock import patch

from spirit.database import db_manager


ADMIN_COOKIE = ""


def call(method, path, body=None, cookie=None):
    from spirit.server.admin_api import route_admin
    headers = {"Cookie": ADMIN_COOKIE if cookie is None else cookie}
    result = route_admin(method, path,
                         json.dumps(body) if body is not None else None,
                         headers=headers)
    status, payload, ctype = result[:3]
    if ctype.startswith('application/json'):
        return status, json.loads(payload)
    return status, payload


def login(username, password):
    """Logs into the admin API; returns (status, data, cookie)."""
    from spirit.server.admin_api import route_admin
    result = route_admin('POST', '/admin/api/login',
                         json.dumps({"username": username, "password": password}),
                         headers={})
    status, payload = result[0], json.loads(result[1])
    cookie = ""
    if len(result) == 4:
        for name, value in result[3]:
            if name == 'Set-Cookie':
                cookie = value.split(';')[0]
    return status, payload, cookie


class TestAdminAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_fd, cls.db_path = tempfile.mkstemp()
        cls.db_patcher = patch('spirit.database.connection.DB_PATH', cls.db_path)
        cls.db_patcher.start()

        from spirit.database.setup_db import setup_database
        setup_database()

        global ADMIN_COOKIE
        status, data, ADMIN_COOKIE = login("brandon", "password")
        assert status == 200 and data["ok"], "seeded admin login failed"

    @classmethod
    def tearDownClass(cls):
        cls.db_patcher.stop()
        try:
            os.close(cls.db_fd)
            os.unlink(cls.db_path)
        except OSError:
            pass

    def test_dashboard_served(self):
        status, payload = call('GET', '/admin')
        self.assertEqual(status, 200)
        self.assertIn(b'SpiritPTCGO', payload)

    def test_overview(self):
        status, data = call('GET', '/admin/api/overview')
        self.assertEqual(status, 200)
        self.assertTrue(data["ok"])
        self.assertIn("SWSH12", data["eligible_sets"])
        self.assertNotIn("BW1", data["eligible_sets"])

    def test_code_lifecycle(self):
        # Generate
        status, data = call('POST', '/admin/api/codes', {
            "reward": {"coins": 500, "products": {}}, "max_uses": 5
        })
        self.assertEqual(status, 200)
        code = data["codes"][0]["code_string"]
        self.assertTrue(code.startswith("SPIRIT-"))

        # List
        status, data = call('GET', '/admin/api/codes')
        self.assertIn(code, [c["code_string"] for c in data["codes"]])

        # Update / disable
        status, data = call('POST', '/admin/api/codes/update', {"code": code, "enabled": False})
        self.assertEqual(status, 200)
        self.assertFalse(data["code"]["enabled"])

        # Duplicate rejected
        status, _ = call('POST', '/admin/api/codes', {"code": code, "reward": {}})
        self.assertEqual(status, 409)

        # Delete
        status, data = call('POST', '/admin/api/codes/delete', {"code": code})
        self.assertEqual(status, 200)

    def test_shop_item_lifecycle(self):
        status, data = call('POST', '/admin/api/shop', {
            "product_guid": "d017c195-83c5-c74e-0638-25128b3116c4",
            "display_name": "Fusion Strike Pack",
            "price": 150, "featured": True
        })
        self.assertEqual(status, 200)
        item_id = data["item"]["id"]
        self.assertTrue(data["item"]["enabled"])
        self.assertTrue(data["item"]["featured"])

        status, data = call('POST', '/admin/api/shop/toggle', {"id": item_id})
        self.assertFalse(data["item"]["enabled"])

        status, data = call('GET', '/admin/api/shop')
        self.assertIn(item_id, [i["id"] for i in data["items"]])

        status, _ = call('POST', '/admin/api/shop/delete', {"id": item_id})
        self.assertEqual(status, 200)

    def test_dynamic_page_lifecycle(self):
        content = {"template": "LandingPageRight",
                   "labels": {"GameText": {"bundle": {"en_US": "Hello"}}}}
        status, data = call('POST', '/admin/api/pages', {
            "content_json": content, "sort_order": 2
        })
        self.assertEqual(status, 200)
        page_id = data["page"]["id"]
        self.assertEqual(data["page"]["content_json"]["template"], "LandingPageRight")

        status, data = call('GET', '/admin/api/pages')
        self.assertIn(page_id, [p["id"] for p in data["pages"]])

        status, _ = call('POST', '/admin/api/pages/delete', {"id": page_id})
        self.assertEqual(status, 200)

    def test_products_listing(self):
        status, data = call('GET', '/admin/api/products')
        self.assertEqual(status, 200)
        keys = {p["key"] for p in data["products"]}
        self.assertIn("SWSH12", keys)  # auto-generated booster present

    def test_grant_all_cards(self):
        from spirit.database.accounts import create_account
        from spirit.database.player_data import get_collection_by_account_id
        from spirit.game.scripts.cards import loader as card_loader

        account = create_account("grant_all_tester", "pw123")
        account_id = account["account_id"]

        status, data = call('POST', '/admin/api/accounts/grant-all-cards',
                            {"account_id": account_id, "count": 4})
        self.assertEqual(status, 200)
        expected = sum(1 for c in card_loader.load_all() if c.key != "Free_Energy")
        self.assertEqual(data["granted"], expected)

        collection = {c["archetype_id"]: c for c in get_collection_by_account_id(account_id)}
        for card in card_loader.load_all():
            if card.key == "Free_Energy":
                continue
            self.assertGreaterEqual(collection[card.guid]["tradable_count"], 4)

    def test_grant_all_cards_bad_account(self):
        status, _ = call('POST', '/admin/api/accounts/grant-all-cards',
                         {"account_id": "does-not-exist"})
        self.assertEqual(status, 404)

    def test_unknown_route(self):
        status, data = call('GET', '/admin/api/nonsense')
        self.assertEqual(status, 404)

    # ---------------- auth ----------------

    def test_api_requires_auth(self):
        status, data = call('GET', '/admin/api/overview', cookie="")
        self.assertEqual(status, 401)
        status, data = call('POST', '/admin/api/codes', {"reward": {}}, cookie="spirit_admin=bogus")
        self.assertEqual(status, 401)

    def test_dashboard_html_is_public(self):
        status, payload = call('GET', '/admin', cookie="")
        self.assertEqual(status, 200)

    def test_login_rejects_bad_credentials_and_non_admin(self):
        status, data, _ = login("brandon", "wrongpassword")
        self.assertEqual(status, 401)
        # a non-admin account can't log in once an admin exists
        from spirit.database.accounts import create_account
        create_account("plain_user", "pw123")
        status, data, _ = login("plain_user", "pw123")
        self.assertEqual(status, 401)

    def test_session_endpoint(self):
        status, data = call('GET', '/admin/api/session')
        self.assertTrue(data["authenticated"])
        self.assertEqual(data["username"], "brandon")
        status, data = call('GET', '/admin/api/session', cookie="")
        self.assertFalse(data["authenticated"])

    def test_set_admin(self):
        from spirit.database.accounts import create_account, get_account_by_username
        acc = create_account("promo_user", "pw123") or get_account_by_username("promo_user")
        status, data = call('POST', '/admin/api/accounts/set-admin',
                            {"account_id": acc["account_id"], "is_admin": True})
        self.assertEqual(status, 200)
        status, data, cookie = login("promo_user", "pw123")
        self.assertEqual(status, 200)
        self.assertTrue(cookie)
        call('POST', '/admin/api/accounts/set-admin',
             {"account_id": acc["account_id"], "is_admin": False})

    # ---------------- tournaments ----------------

    def _tournament_definition(self):
        return {
            "name": "AdminTest Cup", "title": "AdminTest Cup", "description": "test",
            "previewTime": 1, "startTime": 2, "entryClosingTime": 4102444800000,
            "resolutionTime": 4102444800001, "disappearTime": 4102444800002,
            "maxRuns": 3, "prizeBy": "wins",
            "run": {
                "entryFee": [{"currency": "Tokens", "amount": 10}],
                "allowDeckSwitching": True,
                "maxWins": 3, "maxLosses": 2, "maxGames": 0,
                "prizeTable": [
                    {"start": 0, "end": 2, "rewards": [
                        {"rewardType": "Tokens", "rewardAmount": 50}]},
                    {"start": 3, "end": 3, "rewards": [
                        {"rewardType": "Tokens", "rewardAmount": 500}]},
                ],
            },
            "leaderboard": {"runs": 0, "winValue": 3, "lossValue": 1, "prizeTable": []},
        }

    def test_tournament_lifecycle(self):
        status, data = call('POST', '/admin/api/tournaments',
                            {"definition": self._tournament_definition()})
        self.assertEqual(status, 200)
        tid = data["tournament"]["tournament_id"]

        from spirit.game.tournament_manager import TournamentManager
        self.assertIsNotNone(TournamentManager().get(tid))

        status, data = call('GET', '/admin/api/tournaments')
        self.assertIn(tid, [t["tournament_id"] for t in data["tournaments"]])

        status, data = call('POST', '/admin/api/tournaments/toggle', {"tournament_id": tid})
        self.assertFalse(data["tournament"]["enabled"])

        status, data = call('GET', '/admin/api/tournaments/standings/' + tid)
        self.assertEqual(status, 200)
        self.assertEqual(data["standings"], [])

        status, _ = call('POST', '/admin/api/tournaments/delete', {"tournament_id": tid})
        self.assertEqual(status, 200)
        self.assertIsNone(TournamentManager().get(tid))

    def test_tournament_validation(self):
        bad = self._tournament_definition()
        bad["run"]["maxWins"] = 0
        bad["run"]["maxLosses"] = 0
        status, _ = call('POST', '/admin/api/tournaments', {"definition": bad})
        self.assertEqual(status, 400)

        bad = self._tournament_definition()
        bad["run"]["prizeTable"][0]["rewards"] = [{"rewardType": "Archetype"}]
        status, _ = call('POST', '/admin/api/tournaments', {"definition": bad})
        self.assertEqual(status, 400)

        status, _ = call('POST', '/admin/api/tournaments', {"definition": {"name": ""}})
        self.assertEqual(status, 400)

    def test_card_search_and_image(self):
        status, data = call('POST', '/admin/api/cards/search', {"query": "lugia"})
        self.assertEqual(status, 200)
        self.assertTrue(data["cards"])
        self.assertIn("image", data["cards"][0])
        with_image = next((c for c in data["cards"] if c["image"]), None)
        self.assertIsNotNone(with_image)
        status, payload = call('GET', with_image["image"])
        self.assertEqual(status, 200)
        self.assertTrue(payload.startswith(b'\x89PNG'))

    def test_card_image_rejects_traversal(self):
        status, _ = call('GET', '/admin/api/card-image/../secret/1')
        self.assertEqual(status, 400)
        status, _ = call('GET', '/admin/api/card-image/NOSET/999')
        self.assertEqual(status, 404)

    def test_cards_lookup(self):
        status, data = call('POST', '/admin/api/cards/search', {"query": "lugia"})
        guid = data["cards"][0]["guid"]
        status, data = call('POST', '/admin/api/cards/lookup', {"guids": [guid.upper()]})
        self.assertEqual(status, 200)
        self.assertIn(guid.lower(), data["cards"])
        self.assertTrue(data["cards"][guid.lower()]["name"])

    def test_versus_seasons_roundtrip(self):
        from spirit.game import season_manager
        fd, path = tempfile.mkstemp(suffix='.json')
        os.close(fd)
        try:
            with open(path, 'w') as f:
                f.write('[]')
            with patch('spirit.game.season_manager.SEASONS_PATH', path):
                payload = {"seasons": [{
                    "seasonID": "TestSeason", "startTime": 0, "endTime": 4102444800000,
                    "description": {"id": "Test Season"},
                    "tiers": [{"rewards": {"10": [
                        {"name": "5 Tokens", "rewardType": "Tokens",
                         "rewardAmount": 5, "rewardCurrency": "prizeTrainerCoin"},
                        {"name": "Reward Card", "rewardType": "Archetype",
                         "rewardAmount": 2, "rewardProductID": "abc-123",
                         "rewardDescription": {"id": "Reward Card"}}
                    ]}}],
                    "resetRewardID": ""
                }]}
                status, data = call('POST', '/admin/api/versus-seasons', payload)
                self.assertEqual(status, 200)

                status, data = call('GET', '/admin/api/versus-seasons')
                self.assertEqual(status, 200)
                self.assertEqual(data["seasons"][0]["seasonID"], "TestSeason")
                # normalized wire order: archetypes first, tokens last, indexed
                rewards = data["seasons"][0]["tiers"][0]["rewards"]["10"]
                self.assertEqual(rewards[0]["rewardType"], "Archetype")
                self.assertEqual(rewards[0]["rewardProductID"], "abc-123")
                self.assertEqual(rewards[0]["index"], 0)
                self.assertEqual(rewards[1]["rewardType"], "Tokens")
                self.assertIsNone(rewards[1]["rewardProductID"])
                self.assertEqual(rewards[1]["index"], 1)

                # hot reload picked up the new config
                mgr = season_manager.VersusSeasonManager()
                self.assertEqual(mgr.seasons[0].season_id, "TestSeason")
        finally:
            os.unlink(path)
            season_manager.VersusSeasonManager().load_seasons()

    def test_versus_seasons_validation(self):
        status, _ = call('POST', '/admin/api/versus-seasons', {"seasons": []})
        self.assertEqual(status, 400)
        status, _ = call('POST', '/admin/api/versus-seasons',
                         {"seasons": [{"seasonID": ""}]})
        self.assertEqual(status, 400)
        status, _ = call('POST', '/admin/api/versus-seasons', {"seasons": [{
            "seasonID": "S", "tiers": [{"rewards": {"10": [
                {"name": "Card", "rewardType": "Archetype", "rewardAmount": 1}
            ]}}]
        }]})
        self.assertEqual(status, 400)  # Archetype reward missing rewardProductID

        # client crash guard: multi-reward milestone with no card/product
        status, _ = call('POST', '/admin/api/versus-seasons', {"seasons": [{
            "seasonID": "S", "tiers": [{"rewards": {"10": [
                {"name": "5 Tokens", "rewardType": "Tokens", "rewardAmount": 5},
                {"name": "10 Tokens", "rewardType": "Tokens", "rewardAmount": 10}
            ]}}]
        }]})
        self.assertEqual(status, 400)


if __name__ == '__main__':
    unittest.main()
