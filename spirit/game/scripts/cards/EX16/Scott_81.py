from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import scott_search

card = SupporterCardDef(
    guid="8a04dc42-a913-55c4-81d3-a7a3d486c6d0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Scott.Name",
    display_name="Scott",
    searchable_by=["Scott", "Supporter"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=scott_search,
)
