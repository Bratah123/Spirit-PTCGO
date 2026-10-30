"""STUB: effect not implemented — do not guess mechanics.
Dewgong δ (EX15 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_protection_vs_delta, surge_if_water2
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="d723e02f-a6c7-5cf1-9da7-b7359ad6f4a3",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong δ",
    searchable_by=["Dewgong \u03b4", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=87,
    abilities=[
        Ability(
            title="Delta Protection",
            game_text="Any damage done to Dewgong by attacks from your opponent's Pok\u00e9mon that has \u03b4 on its card is reduced by 40 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=delta_protection_vs_delta(),
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Surge",
            game_text="If Dewgong has at least 2 Water Energy attached to it, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=surge_if_water2(40, 20),
        ),
    ],
)