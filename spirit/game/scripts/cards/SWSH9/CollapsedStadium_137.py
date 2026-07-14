from spirit.game.card_effects.trainers import CollapsedStadiumPassive
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    passive=CollapsedStadiumPassive(),
    guid="186e6382-ea02-52af-b518-e47e75df7f50",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CollapsedStadium.Name",
    display_name="Collapsed Stadium",
    searchable_by=["Collapsed Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=137,
    set_code="SWSH9",
    rarity=Rarities.Uncommon
)
