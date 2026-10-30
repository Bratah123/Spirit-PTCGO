"""STUB: effect not implemented — do not guess mechanics.
Cherubi (DP7 #56): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea07e0ac-0bdd-5911-91c3-9f8d40bfa172",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    display_name="Cherubi",
    searchable_by=["Cherubi", "Basic", "Cherubi"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=420,
    abilities=[
        Attack(
            title="Nap",
            game_text="Remove 2 damage counters from Cherubi.",
            cost={},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bullet Seed",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)