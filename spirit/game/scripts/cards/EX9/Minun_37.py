"""STUB: effect not implemented — do not guess mechanics.
Minun (EX9 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import electro_guard_passive


card = PokemonCardDef(
    guid="351dfdf8-7cf9-5bc0-8b1c-29759aeea7fd",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minun.Name",
    display_name="Minun",
    searchable_by=["Minun", "Basic", "Minun"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=312,
    abilities=[
        Ability(
            title="Electro-guard",
            game_text="As long Minun has any Lightning Energy attached to it, Minun has no Weakness.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=electro_guard_passive(),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=flip_bonus(20),
        ),
    ],
)