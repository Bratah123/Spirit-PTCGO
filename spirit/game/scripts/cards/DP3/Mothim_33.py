"""STUB: effect not implemented — do not guess mechanics.
Mothim (DP3 #33): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b3972ce7-57a3-5c63-abdb-6430f0efb6f5",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mothim.Name",
    display_name="Mothim",
    searchable_by=["Mothim", "Stage 1", "Mothim"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="DP3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name",
    family_id=414,
    abilities=[
        Attack(
            title="Silver Wind",
            game_text="During your next turn, if an attack does damage to the Defending Pok\u00e9mon (after applying Weakness and Resistance), that attack does 40 more damage.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Raging Scales",
            game_text="If Mothim has any damage counters on it, this attack does 30 damage plus 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)