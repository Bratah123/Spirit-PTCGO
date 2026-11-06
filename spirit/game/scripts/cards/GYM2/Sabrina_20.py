from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import sabrina, sabrina_condition


card = ItemCardDef(
    guid="69ea82da-eaef-5520-9381-7ee0353710e6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sabrina.Name",
    display_name="Sabrina",
    searchable_by=["Sabrina"],
    subtypes=[],
    collector_number=20,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    condition=sabrina_condition,
    effect=sabrina,
)
