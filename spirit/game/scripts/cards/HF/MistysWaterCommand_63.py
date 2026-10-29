from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.hf import (
    mistys_water_command, mistys_water_command_condition,
)

card = SupporterCardDef(
    guid="5ee0e1b4-cc2f-5626-9bb6-4548f3ba703d",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWaterCommand.Name",
    display_name="Misty's Water Command",
    searchable_by=["Misty's Water Command", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="HF",
    rarity=Rarities.RareHolo,
    effect=mistys_water_command,
    condition=mistys_water_command_condition,
)
