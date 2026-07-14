from spirit.game.card_effects.trainers import SkatersParkPassive
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="efea575e-8cd8-5c71-9b51-81b59d2c3400",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkatersPark.Name",
    display_name="Skaters' Park",
    searchable_by=["Skaters' Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=242,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    passive=SkatersParkPassive(),
)
