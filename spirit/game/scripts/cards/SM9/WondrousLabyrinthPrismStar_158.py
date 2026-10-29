from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    wondrous_labyrinth_passive,
)

card = StadiumCardDef(
    guid="d51677c0-4efd-53b4-b1fb-50b59414cb3e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousLabyrinthPrismStar.Name",
    display_name="Wondrous Labyrinth {*}",
    searchable_by=["Wondrous Labyrinth {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=158,
    set_code="SM9",
    rarity=Rarities.Prism,
            passive=wondrous_labyrinth_passive,
        )
