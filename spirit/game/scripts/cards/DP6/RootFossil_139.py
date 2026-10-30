"""Root Fossil (DP6 #139)."""
from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="e9dfe1c6-e7aa-59f8-93ef-294edcc65065",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
