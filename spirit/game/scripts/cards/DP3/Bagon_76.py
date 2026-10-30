"""STUB: effect not implemented — do not guess mechanics.
Bagon (DP3 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="544ec217-fb16-5fa0-88ed-994fb4751cb6",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=371,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Bagon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)