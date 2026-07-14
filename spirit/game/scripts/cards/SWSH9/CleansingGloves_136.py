from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    passive=typed_damage_boost_tool(PokemonTypes.PSYCHIC, 30),
    guid="ea5c50f9-648e-55ea-984b-e412933de360",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CleansingGloves.Name",
    display_name="Cleansing Gloves",
    searchable_by=["Cleansing Gloves", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=136,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
)
