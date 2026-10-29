from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import bonnie, bonnie_condition

card = SupporterCardDef(
    guid="60d0a3af-5b9c-5c67-8aba-bff059e62847",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name",
    display_name="Bonnie",
    searchable_by=["Bonnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=bonnie_condition,
    effect=bonnie,
)
