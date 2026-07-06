from spirit.game.card_effects.trainers import gardenias_vigor
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9e9b0b3b-a3b3-54ee-ab8e-5d353619db1c",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GardeniasVigor.Name",
    display_name="Gardenia's Vigor",
    searchable_by=["Gardenia's Vigor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=gardenias_vigor
)
