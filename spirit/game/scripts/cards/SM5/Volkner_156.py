from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import volkner

card = SupporterCardDef(
    guid="a96066ea-4d1f-5671-acd4-712921ce6500",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Volkner.Name",
    display_name="Volkner",
    searchable_by=["Volkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=156,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    effect=volkner,
)
