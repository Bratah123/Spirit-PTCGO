from spirit.game.data_utils import PokemonToolCardDef, is_pokemon_v, def_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import attack_discount_passive

_ELEMENTAL_BADGE_NAMES = ("Vaporeon", "Jolteon", "Flareon")


def _elemental_badge_pred(pokemon):
    if not is_pokemon_v(pokemon.archetype_id):
        return False
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return any(n in name for n in _ELEMENTAL_BADGE_NAMES)


card = PokemonToolCardDef(
    guid="de6e7629-b576-54c9-8c98-cdbda7ec87fa",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElementalBadge.Name",
    display_name="Elemental Badge",
    searchable_by=["Elemental Badge", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=147,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=attack_discount_passive(1, pred=_elemental_badge_pred),
)
