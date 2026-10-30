"""Old Amber (DP5 #84)."""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="03b1abf8-58fa-542e-8949-b41088965dd1",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldAmber.Name",
    display_name="Old Amber",
    searchable_by=["Old Amber", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
