"""STUB: effect not implemented — do not guess mechanics.
Electrode (DP7 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack


card = PokemonCardDef(
    guid="953426bd-3253-521b-8f53-77213b783cce",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Flash",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Electro Diffusion",
            game_text="Does 40 damage plus 10 more damage for each Lightning Energy attached to Electrode. Flip a coin. If tails, discard all Lightning Energy attached to Electrode.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)