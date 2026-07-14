from spirit.game.card_effects.passives_common import ability_lock_passive
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_water_pokemon


def _has_memory_capsule(carrier):
    for child in carrier.children:
        d = def_for(child.archetype_id)
        if d and d.display_name == "Memory Capsule":
            return True
    return False


def _water_locked(pokemon, carrier):
    return _has_memory_capsule(carrier) and is_water_pokemon(pokemon)

card = PokemonCardDef(
    guid="ef51ea27-9a73-5ffa-8faf-1cb81b807524",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Jolteon"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Thunderous Awakening",
            game_text="If this Pok\u00e9mon has a Memory Capsule attached, Water Pok\u00e9mon in play (both yours and your opponent's) have no Abilities.",
            passive=ability_lock_passive(_water_locked),
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)