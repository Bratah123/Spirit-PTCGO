from spirit.game.card_effects.trainers import bede, bede_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8fea1e13-0d34-54ed-92e0-5a42f8c231bd",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bede.Name",
    display_name="Bede",
    searchable_by=["Bede", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    effect=bede,
    condition=bede_playable
)
