from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import misty, misty_condition


card = ItemCardDef(
    guid="ef622217-068c-5818-9591-e1f69689b011",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=18,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    condition=misty_condition,
    effect=misty,
)
