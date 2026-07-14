from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="ddddd6e8-b9a3-52c9-8b10-4a89518534ef",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VitalityBand.Name",
    display_name="Vitality Band",
    searchable_by=["Vitality Band", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=185,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(lambda t: True, 10),
)
