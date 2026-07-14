from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="3cb5b10a-d183-5ede-938f-21e9195bfe0c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpongyGloves.Name",
    display_name="Spongy Gloves",
    searchable_by=["Spongy Gloves", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00c3\u00a9mon Tool"],
    collector_number=243,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(PokemonTypes.WATER, 30),
)
