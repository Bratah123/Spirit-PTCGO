from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="dc156368-3e76-5529-baa8-1bb8ff6a06a1",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DiggingGloves.Name",
    display_name="Digging Gloves",
    searchable_by=["Digging Gloves", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=145,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.FIGHTING, 30),
)
