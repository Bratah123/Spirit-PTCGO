from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="6f87ca9b-9918-5450-875e-c3a58747d324",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireResistantGloves.Name",
    display_name="Fire-Resistant Gloves",
    searchable_by=["Fire-Resistant Gloves", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=138,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.FIRE, 30),
)
