from spirit.game.card_effects.trainers import bede, bede_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="fddc2de4-aed1-565d-a95a-67fae0d5eab5",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bede.Name",
    display_name="Bede",
    searchable_by=["Bede", "Supporter"],
    subtypes=["Supporter"],
    collector_number=207,
    set_code="SWSH1",
    rarity=Rarities.RareRainbow,
    effect=bede,
    condition=bede_playable
)
