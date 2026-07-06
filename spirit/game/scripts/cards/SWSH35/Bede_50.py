from spirit.game.card_effects.trainers import bede, bede_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="82f53f59-ae40-5b37-a98c-b24781324775",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bede.Name",
    display_name="Bede",
    searchable_by=["Bede", "Supporter"],
    subtypes=["Supporter"],
    collector_number=50,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=bede,
    condition=bede_playable
)
