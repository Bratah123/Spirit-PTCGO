from spirit.game.card_effects.trainers import bede, bede_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9a29ed1f-2288-5cbb-ae10-dde38f518684",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bede.Name",
    display_name="Bede",
    searchable_by=["Bede", "Supporter"],
    subtypes=["Supporter"],
    collector_number=199,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    effect=bede,
    condition=bede_playable
)
