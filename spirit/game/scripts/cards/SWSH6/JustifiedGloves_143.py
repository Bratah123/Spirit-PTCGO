from spirit.game.card_effects.passives_common import typed_damage_boost_tool
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = PokemonToolCardDef(
    guid="37b01399-320a-5640-a850-22dd6a87ae6f",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JustifiedGloves.Name",
    display_name="Justified Gloves",
    searchable_by=["Justified Gloves", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=143,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.DARKNESS, 30)
)
