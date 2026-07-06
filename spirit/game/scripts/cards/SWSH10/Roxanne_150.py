from spirit.game.card_effects.trainers import opponent_prizes_low, roxanne
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c61c9472-3e50-5a8d-880b-dbda110b6878",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxanne.Name",
    display_name="Roxanne",
    searchable_by=["Roxanne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=roxanne,
    condition=opponent_prizes_low
)
