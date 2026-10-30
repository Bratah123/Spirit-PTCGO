"""STUB: effect not implemented — do not guess mechanics.
Vibrava δ (EX15 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import psychic_wing_retreat0_if_psychic
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="15aa3adb-d544-5487-b0e3-084c57ef2c76",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava δ",
    searchable_by=["Vibrava \u03b4", "Stage 1", "Vibrava"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=329,
    abilities=[
        Ability(
            title="Psychic Wing",
            game_text="If Vibrava has any Psychic Energy attached to it, the Retreat Cost for Vibrava is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=psychic_wing_retreat0_if_psychic(),
        ),
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)