from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import fossil_search
from spirit.game.session.effects import is_pokemon_card


def _amaura_or_tyrunt(card):
    return is_pokemon_card(card) and getattr(
        def_for(card.archetype_id), "display_name", None) in ("Amaura", "Tyrunt")


card = SupporterCardDef(
    guid="c51e44de-fa49-56c8-a267-cad4ceeb693a",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilResearcher.Name",
    display_name="Fossil Researcher",
    searchable_by=["Fossil Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="XY3",
    rarity=Rarities.RareUltra,
    effect=fossil_search(_amaura_or_tyrunt, count=2, label='Amaura or Tyrunt')
)
