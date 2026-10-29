from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(
    guid="97458d5c-c30e-5972-9922-30ecf7b16f65",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name",
    display_name="Unidentified Fossil",
    searchable_by=["Unidentified Fossil", "Item"],
    subtypes=["Item"],
    collector_number=207,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=60,
    passive=FossilBodyPassive(),
    abilities=[fossil_discard_ability()],
)
