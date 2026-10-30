from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import misty, misty_condition


card = ItemCardDef(
    guid="95817130-6a28-598b-8901-6792f50d7d9f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=102,
    set_code="GYM1",
    rarity=Rarities.Rare,
    condition=misty_condition,
    effect=misty,
)
