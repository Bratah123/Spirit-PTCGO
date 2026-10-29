from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import lysandre_prism_star, lysandre_prism_star_condition

card = SupporterCardDef(
    guid="89bf6e51-6769-5f5b-b1b4-f0aec5c9ea0c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandrePrismStar.Name",
    display_name="Lysandre {*}",
    searchable_by=["Lysandre {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=110,
    set_code="SM6",
    rarity=Rarities.Prism,
    condition=lysandre_prism_star_condition,
    effect=lysandre_prism_star,
)
