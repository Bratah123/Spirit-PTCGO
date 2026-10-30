"""Maxie_73 wired."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import archie_maxie

card = SupporterCardDef(
    guid="3006348b-81f8-5dab-9f15-6d35351216d8",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maxie.Name",
    display_name="Maxie",
    searchable_by=["Maxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=archie_maxie("Team Magma", from_zones=("hand", "discard"))
)
