from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import clay

card = SupporterCardDef(
    guid="5b24b989-b802-57e1-b96b-4912c7be9eb4",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clay.Name",
    display_name="Clay",
    searchable_by=["Clay", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=clay,
)
