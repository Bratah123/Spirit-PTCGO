from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import mistys_tears, mistys_tears_condition


card = ItemCardDef(
    guid="96464e84-d474-5522-959b-e8322a411ce4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysTears.Name",
    display_name="Misty's Tears",
    searchable_by=["Misty's Tears"],
    subtypes=[],
    collector_number=118,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=mistys_tears_condition,
    effect=mistys_tears,
)
