"""STUB: effect not implemented — do not guess mechanics.
Lotad (DP3 #92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae0b3f2f-b36e-5769-9474-a07719965b60",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name",
    display_name="Lotad",
    searchable_by=["Lotad", "Basic", "Lotad"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=270,
    abilities=[
        Attack(
            title="Water Sport",
            game_text="If Lotad has less Energy attached to it than the Defending Pok\u00e9mon, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)