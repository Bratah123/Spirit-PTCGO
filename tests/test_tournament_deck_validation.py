import unittest
import uuid

from spirit.game.attributes import AttrID, CardType, DeckFormat, PokemonStage
from spirit.game import rules
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.tournament_manager import TournamentDef
from spirit.packets.handlers.tournaments import validate_tournament_deck


class TournamentDeckValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        card_loader.load_all()
        cls.swsh_basic = next(
            card for card in card_loader.cards
            if card.key == "SWSH8"
            and card.get_attribute_value(AttrID.CARD_TYPE) == CardType.POKEMON.value
            and card.get_attribute_value(AttrID.STAGE, 0) == PokemonStage.BASIC.value
        )
        cls.bw_card = next(card for card in card_loader.cards if card.key == "BW1")
        cls.water = next(
            card for card in card_loader.cards
            if card.key == "Free_Energy"
            and rules.card_display_name(card) == "Water Energy"
        )

    def make_deck(self, pile_name="deck", include_bw=False):
        cards = [self.swsh_basic.guid] * 4
        if include_bw:
            cards.append(self.bw_card.guid)
        cards.extend([self.water.guid] * (60 - len(cards)))
        return {
            "deckID": str(uuid.uuid4()),
            "deckName": "Tournament Test",
            "piles": {pile_name: cards},
        }

    def tournament(self, definition):
        return TournamentDef(str(uuid.uuid4()), definition, True)

    def test_legacy_join_accepts_server_and_client_pile_names(self):
        tournament = self.tournament({"format": "Modified"})
        for pile_name in ("deck", "CakePile"):
            results, error = validate_tournament_deck(
                self.make_deck(pile_name), tournament, legacy=True)
            self.assertIsNone(error)
            self.assertTrue(results[0]["valid"], pile_name)

    def test_legacy_join_enforces_tournament_format(self):
        tournament = self.tournament({"format": "Modified"})
        results, error = validate_tournament_deck(
            self.make_deck("CakePile", include_bw=True), tournament, legacy=True)
        self.assertIsNone(error)
        self.assertFalse(results[0]["valid"])
        self.assertIn(
            "DeckContainsBannedCards",
            {detail["failureType"] for detail in results[0]["results"]},
        )

    def test_async_game_format_accepts_a_guid(self):
        tournament = self.tournament({
            "format": "Unlimited",
            "game": {"format": DeckFormat.STANDARD.value},
        })
        deck = self.make_deck("CakePile", include_bw=True)
        async_results, async_error = validate_tournament_deck(deck, tournament)
        legacy_results, legacy_error = validate_tournament_deck(
            deck, tournament, legacy=True)
        self.assertIsNone(async_error)
        self.assertIsNone(legacy_error)
        self.assertFalse(async_results[0]["valid"])
        self.assertTrue(legacy_results[0]["valid"])


if __name__ == "__main__":
    unittest.main()
