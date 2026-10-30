"""STUB: effect not implemented — do not guess mechanics.
Masquerain (EX8 #39): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import intimidating_pattern_passive



card = PokemonCardDef(
    guid="24045992-bba6-5a34-a26e-f2934380ea49",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Ability(
            title="Intimidating Pattern",
            game_text="As long as Masquerain is your Active Pok\u00e9mon, any damage done by an opponent's attack is reduced by 20 (before applying Weakness and Resistance). You can't use more than 1 Intimidating Pattern Pok\u00e9-Body each turn.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=intimidating_pattern_passive(),
        ),
        Attack(
            title="Stun Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)