from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import poke_gear


card = ItemCardDef(
    guid="5bb6a32e-1e6e-5218-ac5d-0979cf370797",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeGear.Name",
    display_name="PokéGear",
    searchable_by=["Pok\u00e9Gear"],
    subtypes=[],
    collector_number=88,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=poke_gear
)
