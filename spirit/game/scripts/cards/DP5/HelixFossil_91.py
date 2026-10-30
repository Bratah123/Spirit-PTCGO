"""Helix Fossil (DP5 #91)."""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="c1049325-3e43-5e19-bd5f-fb1ee21324be",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HelixFossil.Name",
    display_name="Helix Fossil",
    searchable_by=["Helix Fossil", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
