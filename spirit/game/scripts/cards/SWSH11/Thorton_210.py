from spirit.game.card_effects.trainers import thorton, thorton_condition
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="220cbaac-4336-5c64-b906-facd90332e3f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Thorton.Name",
    display_name="Thorton",
    searchable_by=["Thorton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    condition=thorton_condition,
    effect=thorton,
)
