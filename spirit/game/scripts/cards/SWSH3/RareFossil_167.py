from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="be893da7-2edb-575b-9220-f38f3f685444",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareFossil.Name",
    display_name="Rare Fossil",
    searchable_by=["Rare Fossil", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=70,
    passive=FossilBodyPassive(blocks_conditions=True),
    abilities=[fossil_discard_ability()],
)
