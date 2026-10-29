from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import metal_frying_pan_passive

card = PokemonToolCardDef(
    guid="52b2b3ca-fdbd-5761-874f-87ec4c16bcf2",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalFryingPan.Name",
    display_name="Metal Frying Pan",
    searchable_by=["Metal Frying Pan", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=112,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    passive=metal_frying_pan_passive,
)
