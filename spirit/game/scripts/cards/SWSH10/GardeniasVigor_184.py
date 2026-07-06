from spirit.game.card_effects.trainers import gardenias_vigor
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8f2558e0-76ea-56f1-89c0-31b4b9468044",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GardeniasVigor.Name",
    display_name="Gardenia's Vigor",
    searchable_by=["Gardenia's Vigor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=184,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=gardenias_vigor
)
