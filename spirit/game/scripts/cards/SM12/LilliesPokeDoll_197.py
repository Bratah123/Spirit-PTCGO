from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import (
    lillies_poke_doll_ability, lillies_poke_doll_passive,
)

card = FossilItemCardDef(
    guid="048b0ead-88e2-50e4-a3bd-39fe77e426f6",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesPokeDoll.Name",
    display_name="Lillie's Poké Doll",
    searchable_by=["Lillie's Pok\u00e9 Doll", "Item"],
    subtypes=["Item"],
    collector_number=197,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=30,
    passive=lillies_poke_doll_passive,
    abilities=[lillies_poke_doll_ability()],
)
card.prize_count = 0
