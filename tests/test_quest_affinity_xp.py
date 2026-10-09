"""Daily challenge affinity XP: per-type routing for Total Level progression."""
import datetime
import unittest
import uuid

from types import SimpleNamespace

from spirit.game.progression.quests import AFFINITIES, XP_LEVELS, load_catalog, quest_payload


def _row(definition, activations=0):
    return SimpleNamespace(quest_id=str(uuid.uuid4()), definition=definition,
                           activations=activations)


class CatalogAffinityTests(unittest.TestCase):
    def test_every_template_carries_a_valid_affinity(self):
        for template in load_catalog():
            self.assertIn(template.get("affinity"), AFFINITIES,
                          f"{template['key']} must name a real type")

    def test_affinity_validation_rejects_unknown_types(self):
        from spirit.game.progression.quests import CATALOG_PATH
        import json
        original = CATALOG_PATH.read_text(encoding="utf-8")
        bad = json.loads(original)
        bad[0]["affinity"] = "NotAType"
        CATALOG_PATH.write_text(json.dumps(bad), encoding="utf-8")
        load_catalog.cache_clear()
        try:
            with self.assertRaises(ValueError):
                load_catalog()
        finally:
            CATALOG_PATH.write_text(original, encoding="utf-8")
            load_catalog.cache_clear()

    def test_quest_payload_reports_template_affinity(self):
        template = dict(load_catalog()[1])  # damage -> Fighting
        payload = quest_payload(_row(template))
        self.assertEqual(payload["questDefinition"]["affinity"], "Fighting")

    def test_legacy_payload_falls_back_to_colorless(self):
        template = {k: v for k, v in load_catalog()[0].items()
                    if k != "affinity"}
        payload = quest_payload(_row(template))
        self.assertEqual(payload["questDefinition"]["affinity"], "Colorless")


class CreditMatchRoutingTests(unittest.TestCase):
    def setUp(self):
        from spirit.database import Base, engine, db_session, Account
        from spirit.database.models import QuestAccount, DailyQuest, QuestMatchCredit
        Base.metadata.create_all(engine)
        self.db_session = db_session
        self.Account = Account
        self.QuestAccount = QuestAccount
        self.DailyQuest = DailyQuest
        self.QuestMatchCredit = QuestMatchCredit
        self.account = str(uuid.uuid4())
        with db_session() as session:
            session.add(Account(account_id=self.account,
                                username=f"qa-{self.account}",
                                password_hash="x", screen_name="QA"))

    def tearDown(self):
        with self.db_session() as session:
            for model in (self.DailyQuest, self.QuestMatchCredit, self.QuestAccount,
                          self.Account):
                session.query(model).filter_by(account_id=self.account).delete()
            from spirit.database import Wallet
            session.query(Wallet).filter_by(account_id=self.account).delete()

    def _activate(self, definition, accepted_at=1.0):
        with self.db_session() as session:
            session.add(self.DailyQuest(
                quest_id=str(uuid.uuid4()), account_id=self.account,
                offered_date=datetime.date.today(), status="active",
                definition=definition, activations=0, accepted_at=accepted_at))

    def _credit(self, game_id, won=True, started_at=100.0):
        from spirit.database.quests import credit_match
        return credit_match(self.account, game_id,
                            {"wins": int(won)}, won, started_at)

    def _xp_map(self):
        from spirit.database.quests import account_quest_attributes
        return account_quest_attributes(self.account)["xp"]

    def test_xp_routes_to_the_quest_affinity(self):
        template = dict(load_catalog()[0], affinity="Fire")  # first_win, xp 1
        self._activate(template)
        result = self._credit("game-fire-1")
        self.assertEqual(len(result["completedQuestsAndXPTotal"]), 1)
        _, new_xp = result["completedQuestsAndXPTotal"][0]
        self.assertEqual(new_xp, 1)
        xp = self._xp_map()
        self.assertEqual(xp["Fire"], 1)
        self.assertEqual(xp["Colorless"], 0, "other types stay untouched")

    def test_level_up_grant_is_tagged_with_the_quest_affinity(self):
        template = dict(load_catalog()[0], affinity="Water",
                        xp=XP_LEVELS[1])  # crosses level 1 in one completion
        self._activate(template)
        result = self._credit("game-water-1")
        level_grants = [r for r in result["rewards"]
                        if r["rewardSource"] == "WaterLevel1"]
        self.assertEqual(len(level_grants), 1)
        from spirit.database import db_session, Wallet
        with db_session() as session:
            wallet = session.query(Wallet).filter_by(
                account_id=self.account).first()
            coins = wallet.coins
        # template coins + the 25-coin level-up grant
        self.assertEqual(coins, template["coins"] + 25)

    def test_legacy_definition_without_affinity_stays_colorless(self):
        template = {k: v for k, v in load_catalog()[0].items()
                    if k != "affinity"}
        template["xp"] = XP_LEVELS[1]
        self._activate(template)
        self._credit("game-legacy-1")
        xp = self._xp_map()
        self.assertEqual(xp["Colorless"], XP_LEVELS[1])
        self.assertEqual(xp["Fire"], 0)

    def test_each_catalog_affinity_is_independently_trackable(self):
        for base in load_catalog():
            self._activate(dict(base))
        from spirit.database.quests import credit_match
        credit_match(self.account, "game-all",
                     {"wins": 1, "damagedealt": 500, "energyplayed": 5,
                      "trainersplayed": 10, "prizecardstaken": 6},
                     True, 100.0)
        xp = self._xp_map()
        expected = {t["affinity"] for t in load_catalog()}
        for affinity in AFFINITIES:
            want = 1 if affinity in expected else 0
            self.assertEqual(xp[affinity], want,
                             f"{affinity} XP should be {want}")


if __name__ == "__main__":
    unittest.main()
