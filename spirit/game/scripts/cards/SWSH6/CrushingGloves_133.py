from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="0e54da48-550c-5772-a434-30181fbbd2ab",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingGloves.Name",
    display_name="Crushing Gloves",
    searchable_by=["Crushing Gloves", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=133,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.METAL, 30)
)
