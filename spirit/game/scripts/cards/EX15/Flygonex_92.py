"""STUB: effect not implemented — do not guess mechanics.
Flygon ex δ (EX15 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import clay_pulse, sand_damage_between_turns


card = PokemonCardDef(
    guid="6b5dba0b-2c1d-5781-bf75-f37a0c448a5e",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygonex.Name",
    display_name="Flygon ex δ",
    searchable_by=["Flygon ex \u03b4", "Stage 2", "ex", "Flygonex"],
    subtypes=["Stage 2", "ex"],
    collector_number=92,
    set_code="EX15",
    rarity=Rarities.RareHoloEX,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=330,
    abilities=[
        Ability(
            title="Sand Damage",
            game_text="As long as Flygon ex is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Benched Basic Pok\u00e9mon between turns. You can't use more than 1 Sand Damage Pok\u00e9-Body between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            effect=sand_damage_between_turns(1),
        ),
        Attack(
            title="Psychic Pulse",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            # STUB: attack effect not implemented
            effect=clay_pulse(),
        ),
    ],
)