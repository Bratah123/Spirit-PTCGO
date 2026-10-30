"""Dome Fossil (DP5 #89)."""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="e0327650-e169-57b9-abdb-fbf3e5a73c32",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DomeFossil.Name",
    display_name="Dome Fossil",
    searchable_by=["Dome Fossil", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
