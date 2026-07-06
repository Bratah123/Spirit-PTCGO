from spirit.game.card_effects.trainers import gardenias_vigor
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="23be791a-7adb-522c-b5ea-693a2e15e613",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GardeniasVigor.Name",
    display_name="Gardenia's Vigor",
    searchable_by=["Gardenia's Vigor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=202,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=gardenias_vigor
)
