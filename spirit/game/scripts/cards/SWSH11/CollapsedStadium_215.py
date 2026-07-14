from spirit.game.card_effects.trainers import CollapsedStadiumPassive
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    passive=CollapsedStadiumPassive(),
    guid="0fcfbb09-dce2-5b59-b0ea-7d90778a6fdd",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CollapsedStadium.Name",
    display_name="Collapsed Stadium",
    searchable_by=["Collapsed Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=215,
    set_code="SWSH11",
    rarity=Rarities.RareSecret
)
