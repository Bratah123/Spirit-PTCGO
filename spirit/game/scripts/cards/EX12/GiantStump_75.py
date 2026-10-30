"""EX12 Legend Maker — Giant Stump stadium.
"""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import giant_stump_passive


card = StadiumCardDef(
    guid="3fd75fd0-ef97-5631-9870-02e27e2a7fb2",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantStump.Name",
    display_name="Giant Stump",
    searchable_by=["Giant Stump", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    passive=giant_stump_passive(),
)
