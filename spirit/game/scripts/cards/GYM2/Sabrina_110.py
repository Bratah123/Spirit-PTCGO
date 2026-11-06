from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import sabrina, sabrina_condition


card = ItemCardDef(
    guid="7ea5ea75-851e-5c85-b8e3-3b6741381fb6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sabrina.Name",
    display_name="Sabrina",
    searchable_by=["Sabrina"],
    subtypes=[],
    collector_number=110,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=sabrina_condition,
    effect=sabrina,
)
