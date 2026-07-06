from spirit.game.card_effects.trainers import PathToThePeakPassive
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    passive=PathToThePeakPassive(),
    guid="b99e0bc2-063c-5165-a2d9-45283bb3deb1",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PathtothePeak.Name",
    display_name="Path to the Peak",
    searchable_by=["Path to the Peak", "Stadium"],
    subtypes=["Stadium"],
    collector_number=148,
    set_code="SWSH6",
    rarity=Rarities.Uncommon
)
