"""STUB: effect not implemented — do not guess mechanics.
M Swampert-EX (Promo_XY #XY87): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8ebaa97-3e82-5031-a140-0c3fd58a0c19",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSwampertEX.Name",
    display_name="M Swampert-EX",
    searchable_by=["M Swampert-EX", "MEGA", "EX", "MSwampertEX"],
    subtypes=["MEGA", "EX"],
    collector_number=87,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SwampertEX.Name",
    family_id=260,
    abilities=[
        Attack(
            title="Strongarm Impact",
            game_text="You may do 30 more damage. If you do, discard the top 3 cards of each player's deck.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)