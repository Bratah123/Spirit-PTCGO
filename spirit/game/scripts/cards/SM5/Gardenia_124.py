from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import gardenia, gardenia_condition

card = SupporterCardDef(
    guid="54942e2f-c703-50ee-b634-7b23d5a46a45",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gardenia.Name",
    display_name="Gardenia",
    searchable_by=["Gardenia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    condition=gardenia_condition,
    effect=gardenia,
)
