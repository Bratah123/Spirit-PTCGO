"""STUB: effect not implemented — do not guess mechanics.
Weezing (EX11 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import body_odor_between_turns, breaking_sound


card = PokemonCardDef(
    guid="8921a105-e79d-5d45-b4e4-611d9bd9e1ee",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Body Odor",
            game_text="As long as Weezing is the Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon that has any Pok\u00e9-Bodies between turns.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=body_odor_between_turns(1),
        ),
        Attack(
            title="Mist Attack",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=breaking_sound(10),
        ),
        Attack(
            title="Sludge Whirlpool",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)