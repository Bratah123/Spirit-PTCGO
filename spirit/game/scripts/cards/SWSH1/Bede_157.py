from spirit.game.card_effects.trainers import bede, bede_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="973e68b3-514d-57d4-a821-2c5b427527eb",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bede.Name",
    display_name="Bede",
    searchable_by=["Bede", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=bede,
    condition=bede_playable
)
