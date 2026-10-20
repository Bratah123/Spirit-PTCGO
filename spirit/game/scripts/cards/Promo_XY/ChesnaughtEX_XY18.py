"""STUB: effect not implemented — do not guess mechanics.
Chesnaught-EX (Promo_XY #XY18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92b55c23-aa06-53e8-a8f4-437bac76270d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChesnaughtEX.Name",
    display_name="Chesnaught-EX",
    searchable_by=["Chesnaught-EX", "Basic", "EX", "ChesnaughtEX"],
    subtypes=["Basic", "EX"],
    collector_number=18,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    family_id=652,
    abilities=[
        Attack(
            title="Pin Missile",
            game_text="Flip 4 coins. This attack does 40 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)