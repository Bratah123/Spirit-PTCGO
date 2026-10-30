"""STUB: effect not implemented — do not guess mechanics.
Beedrill δ (EX11 #1): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import cross_cut, final_sting_ko_paralyze_poison, poke_power_condition


card = PokemonCardDef(
    guid="91628e74-d45c-5243-aec9-b6bfea8f114b",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill δ",
    searchable_by=["Beedrill \u03b4", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Final Sting",
            game_text="Once during your turn (before your attack), you may Knock Out Beedrill. If you do, choose 1 of your opponent's Defending Pok\u00e9mon. That Pok\u00e9mon is now Paralyzed and Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns. This power can't be used if Beedrill is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=final_sting_ko_paralyze_poison(2),
        ),
        Attack(
            title="Super Slash",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 50 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=cross_cut(50, 30),
        ),
    ],
)