from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    lusamine_prism_star,
    lusamine_prism_star_condition,
)

card = SupporterCardDef(
    guid="7b69fe43-db66-5d21-ac4c-038ba1cb2d18",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LusaminePrismStar.Name",
    display_name="Lusamine {*}",
    searchable_by=["Lusamine {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=182,
    set_code="SM8",
    rarity=Rarities.Prism,
    effect=lusamine_prism_star,
    condition=lusamine_prism_star_condition,
)
