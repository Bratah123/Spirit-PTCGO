"""Archie_71 wired."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import archie_maxie

card = SupporterCardDef(
    guid="80e76ab7-4498-54c6-b2e6-6722fa6875e3",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Archie.Name",
    display_name="Archie",
    searchable_by=["Archie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=71,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=archie_maxie("Team Aqua", from_zones=("deck",))
)
