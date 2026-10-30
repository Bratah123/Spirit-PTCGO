from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import holon_research_tower_passive

card = StadiumCardDef(
    guid="d19f95b5-ca44-52b3-8d3a-6fd82c1568ff",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonResearchTower.Name",
    display_name="Holon Research Tower",
    searchable_by=["Holon Research Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    passive=holon_research_tower_passive(),
)
