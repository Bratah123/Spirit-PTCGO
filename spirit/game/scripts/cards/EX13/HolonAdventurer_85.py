"""EX13 Holon Phantoms — Holon Adventurer.
"""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import holon_adventurer


card = SupporterCardDef(
    guid="8312838c-e731-5380-b37e-b6dbadc725fc",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonAdventurer.Name",
    display_name="Holon Adventurer",
    searchable_by=["Holon Adventurer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=holon_adventurer(),
)
