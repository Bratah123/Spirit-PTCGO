"""STUB: effect not implemented — do not guess mechanics.
Finneon (DP7 #61): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a54a50c7-3aa0-57d8-a71c-6122f515adf5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    display_name="Finneon",
    searchable_by=["Finneon", "Basic", "Finneon"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=456,
    abilities=[
        Attack(
            title="Aqua Liner",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mouth Pump",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)