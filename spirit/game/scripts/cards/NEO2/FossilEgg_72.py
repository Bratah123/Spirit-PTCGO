from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import fossil_egg
from spirit.game.card_effects.trainers import bench_has_room


card = ItemCardDef(
    guid="8705713e-33f5-5de5-87af-5a3304666223",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilEgg.Name",
    display_name="Fossil Egg",
    searchable_by=["Fossil Egg"],
    subtypes=[],
    collector_number=72,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    condition=bench_has_room,
    effect=fossil_egg,
)
