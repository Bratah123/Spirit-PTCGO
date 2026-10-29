from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool


def _is_gx_or_ex(target):
    subs = subtypes_for(target.archetype_id)
    return "GX" in subs or "EX" in subs


card = PokemonToolCardDef(
    guid="6b20d3a2-dbad-5db0-b917-83445ba707f0",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBand.Name",
    display_name="Choice Band",
    searchable_by=["Choice Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=162,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    passive=typed_damage_boost_tool(_is_gx_or_ex, 30),
)
