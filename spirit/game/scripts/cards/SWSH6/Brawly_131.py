from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.support_common import search_to_bench


def _is_basic_rapid_strike(card):
    return is_basic_pokemon(card) and "Rapid Strike" in subtypes_for(card.archetype_id)


card = SupporterCardDef(
    guid="b8b1ec19-fc2b-57c6-ad29-8be8590d7c49",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brawly.Name",
    display_name="Brawly",
    searchable_by=["Brawly", "Supporter", "Rapid Strike"],
    subtypes=["Supporter", "Rapid Strike"],
    collector_number=131,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(_is_basic_rapid_strike, count=3),
)
