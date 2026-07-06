from spirit.game.card_effects.trainers import opponent_prizes_low, roxanne
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5e25ee04-7ce6-567a-916a-b7a1744bdf90",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxanne.Name",
    display_name="Roxanne",
    searchable_by=["Roxanne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=roxanne,
    condition=opponent_prizes_low
)
