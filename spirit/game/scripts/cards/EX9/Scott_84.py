from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import scott_search

card = SupporterCardDef(
    guid="fedad97e-c47b-551b-88bf-a60a71c50154",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Scott.Name",
    display_name="Scott",
    searchable_by=["Scott", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=scott_search,
)
