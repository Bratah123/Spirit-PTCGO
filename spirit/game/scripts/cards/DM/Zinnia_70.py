from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import ko_last_turn_condition, zinnia

card = SupporterCardDef(
    guid="107dfa23-b613-506d-86f4-3206fb13cb7a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name",
    display_name="Zinnia",
    searchable_by=["Zinnia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=70,
    set_code="DM",
    rarity=Rarities.RareUltra,
    effect=zinnia,
    condition=ko_last_turn_condition,
)
