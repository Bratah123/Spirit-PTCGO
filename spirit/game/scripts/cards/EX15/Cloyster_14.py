"""STUB: effect not implemented — do not guess mechanics.
Cloyster δ (EX15 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import grind_per_energy, solid_shell_bench_delta_protect
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9bf83354-a1a0-5e74-affe-c0267ffe1653",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster δ",
    searchable_by=["Cloyster \u03b4", "Stage 1", "Cloyster"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    family_id=91,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="Prevent all effects of attacks, including damage, done by your opponent's Pok\u00e9mon to each of your Benched Pok\u00e9mon that has \u03b4 on its card.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=solid_shell_bench_delta_protect(),
        ),
        Attack(
            title="Grind",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Cloyster.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=grind_per_energy(10, 10),
        ),
    ],
)