"""STUB: effect not implemented — do not guess mechanics.
Swablu δ (EX15 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import splash_about
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1fe6aa81-b09b-5695-8bc0-42ce64b392d5",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    display_name="Swablu δ",
    searchable_by=["Swablu \u03b4", "Basic", "Swablu"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=333,
    abilities=[
        Attack(
            title="Splash About",
            game_text="If Swablu has less Energy attached to it than the Defending Pok\u00e9mon, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=splash_about(),
        ),
    ],
)