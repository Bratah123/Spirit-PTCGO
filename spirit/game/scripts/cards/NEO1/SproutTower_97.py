from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import sprout_tower_passive


card = StadiumCardDef(
    guid="f23f97e2-ad14-5c48-82f6-a579786983fa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SproutTower.Name",
    display_name="Sprout Tower",
    searchable_by=["Sprout Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    passive=sprout_tower_passive,
)
