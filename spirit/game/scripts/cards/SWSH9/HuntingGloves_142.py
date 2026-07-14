from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="e629c556-d9dd-5a75-8ee7-8e688411c43c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HuntingGloves.Name",
    display_name="Hunting Gloves",
    searchable_by=["Hunting Gloves", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=142,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.DRAGON, 30),
)
