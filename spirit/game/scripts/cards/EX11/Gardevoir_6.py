"""STUB: effect not implemented — do not guess mechanics.
Gardevoir δ (EX11 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.card_effects.ex import black_magic_base_plus_bench, energy_jump_move_any, poke_power_condition, psychic_rage_snipe
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="dab32318-b040-5ad7-9d6d-0084f2370cd8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir δ",
    searchable_by=["Gardevoir \u03b4", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Energy Jump",
            game_text="Once during your turn (before your attack), you may move an Energy card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Gardevoir is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=energy_jump_move_any(),
        ),
        Attack(
            title="Psychic Rage",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage for each damage counter on Gardevoir to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=psychic_rage_snipe(10),
        ),
        Attack(
            title="Black Magic",
            game_text="Does 10 damage plus 20 more damage times the number of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=black_magic_base_plus_bench(10, 20),
        ),
    ],
)