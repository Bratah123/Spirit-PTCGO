from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import gladion, has_prizes_remaining

card = SupporterCardDef(
    guid="6811ebd2-a4ab-5415-82b2-bb7aef94aefb",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gladion.Name",
    display_name="Gladion",
    searchable_by=["Gladion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=109,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    effect=gladion,
    condition=has_prizes_remaining,
)
