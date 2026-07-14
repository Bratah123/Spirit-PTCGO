from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="d139a85a-f0ea-51e2-ae30-df1e4ff28e69",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeedingGloves.Name",
    display_name="Weeding Gloves",
    searchable_by=["Weeding Gloves", "PokÃ©mon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=155,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.GRASS, 30),
)
