from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import ko_last_turn_condition, lance_prism_star

card = SupporterCardDef(
    guid="e3ebff2a-f53c-550d-afcf-caf8d079d6ab",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LancePrismStar.Name",
    display_name="Lance {*}",
    searchable_by=["Lance {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=61,
    set_code="DM",
    rarity=Rarities.Prism,
    effect=lance_prism_star,
    condition=ko_last_turn_condition,
)
