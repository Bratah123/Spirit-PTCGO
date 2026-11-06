from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.ecard import is_supporter_or_stadium


card = SupporterCardDef(
    guid="426d434b-96f3-56a4-9227-e7ef2e735d67",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RelicHunter.Name",
    display_name="Relic Hunter",
    searchable_by=["Relic Hunter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_supporter_or_stadium, count=2, minimum=0, reveal=True,
        prompt="Choose up to 2 Supporter and/or Stadium cards.",
    ),
)
