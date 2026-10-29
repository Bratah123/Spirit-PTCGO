from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import volkner

card = SupporterCardDef(
    guid="03be53aa-c19f-5a03-b6cf-13c6de2496f4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Volkner.Name",
    display_name="Volkner",
    searchable_by=["Volkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=volkner,
)
