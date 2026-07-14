from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="e9e06f61-c93b-5f12-8f53-969981c60f7e",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=60,
    passive=FossilBodyPassive(),
    abilities=[fossil_discard_ability()],
)
