"""STUB: effect not implemented — do not guess mechanics.
Empoleon (DP5 #17): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp3_golem_29_double_throw


card = PokemonCardDef(
    guid="9cbe64b4-523a-5b96-a779-d9eb7febb9c9",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Dual Splash",
            game_text="Choose 2 of your opponent's Pok\u00e9mon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dp3_golem_29_double_throw(),
        ),
        Attack(
            title="Surf Together",
            game_text="Does 50 damage plus 10 more damage for each of your Benched Pok\u00e9mon. Flip a coin. If tails, this attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)