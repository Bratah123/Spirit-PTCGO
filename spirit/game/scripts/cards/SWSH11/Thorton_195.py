from spirit.game.card_effects.trainers import thorton, thorton_condition
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="18d59a80-bb11-50e8-b755-ea99da0bbc19",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Thorton.Name",
    display_name="Thorton",
    searchable_by=["Thorton", "Supporter"],
    subtypes=["Supporter"],
    collector_number=195,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    condition=thorton_condition,
    effect=thorton,
)
