from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="80e07131-c5de-5aa2-9077-42d702d02f56",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MuscleBand.Name",
    display_name="Muscle Band",
    searchable_by=["Muscle Band", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=121,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(lambda target: True, 20)
)
