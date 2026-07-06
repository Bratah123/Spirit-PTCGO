from spirit.game.card_effects.trainers import serena, serena_playable
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9da91305-afcf-57f7-971a-c0ab57422f13",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Serena.Name",
    display_name="Serena",
    searchable_by=["Serena", "Supporter"],
    subtypes=["Supporter"],
    collector_number=193,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    effect=serena,
    condition=serena_playable
)
