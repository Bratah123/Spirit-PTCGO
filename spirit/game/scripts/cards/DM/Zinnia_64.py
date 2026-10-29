from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import ko_last_turn_condition, zinnia

card = SupporterCardDef(
    guid="1fc05985-a25a-5825-a3eb-e83c8ae36363",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name",
    display_name="Zinnia",
    searchable_by=["Zinnia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="DM",
    rarity=Rarities.Uncommon,
    effect=zinnia,
    condition=ko_last_turn_condition,
)
