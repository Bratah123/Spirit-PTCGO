from spirit.game.data_utils import PokemonToolCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool


def _is_gx_or_ex(target):
    subs = subtypes_for(target.archetype_id)
    return "GX" in subs or "EX" in subs


card = PokemonToolCardDef(
    guid="e1cb70ff-d0a8-5549-8435-8641dcc11ef7",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBand.Name",
    display_name="Choice Band",
    searchable_by=["Choice Band", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=175,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(_is_gx_or_ex, 30),
)
