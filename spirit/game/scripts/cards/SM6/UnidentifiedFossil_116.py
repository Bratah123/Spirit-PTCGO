from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="36f72936-b2e8-5c44-aeea-5fce35f859fd",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=60,
    passive=FossilBodyPassive(),
    abilities=[fossil_discard_ability()],
)
