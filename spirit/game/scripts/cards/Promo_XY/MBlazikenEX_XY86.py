"""STUB: effect not implemented — do not guess mechanics.
M Blaziken-EX (Promo_XY #XY86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="194bdd6e-1fef-5cfc-ae00-78aea9afae6f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBlazikenEX.Name",
    display_name="M Blaziken-EX",
    searchable_by=["M Blaziken-EX", "MEGA", "EX", "MBlazikenEX"],
    subtypes=["MEGA", "EX"],
    collector_number=86,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenEX.Name",
    family_id=257,
    abilities=[
        Attack(
            title="Moonsault Blaze",
            game_text="During your next turn, this Pok\u00e9mon's Moonsault Blaze attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)