from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    black_market_passive,
)

card = StadiumCardDef(
    guid="8713634e-a490-56c7-b72f-a119019d7101",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackMarketPrismStar.Name",
    display_name="Black Market {*}",
    searchable_by=["Black Market {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=134,
    set_code="SM9",
    rarity=Rarities.Prism,
            passive=black_market_passive,
        )
