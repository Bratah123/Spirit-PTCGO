from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import roxie

card = SupporterCardDef(
    guid="82b11538-fc23-5c88-a138-4813890384d9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxie.Name",
    display_name="Roxie",
    searchable_by=["Roxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=roxie,
)
