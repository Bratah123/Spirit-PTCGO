"""STUB: effect not implemented — do not guess mechanics.
Bulbasaur (DP3 #77): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="32c67cc7-5516-54da-8762-31ae1d1f90df",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic", "Bulbasaur"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Shake Vine",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bullet Seed",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)