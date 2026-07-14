from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="ba9c42ae-b2ad-5af1-a3a5-ed5c308692dd",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RubberGloves.Name",
    display_name="Rubber Gloves",
    searchable_by=["Rubber Gloves", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=156,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.LIGHTNING, 30),
)
