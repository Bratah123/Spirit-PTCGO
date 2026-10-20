"""STUB: effect not implemented — do not guess mechanics.
Blaziken-EX (Promo_XY #XY54): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3ce752b-1669-5bdc-afca-79a8da8a9428",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenEX.Name",
    display_name="Blaziken-EX",
    searchable_by=["Blaziken-EX", "Basic", "EX", "BlazikenEX"],
    subtypes=["Basic", "EX"],
    collector_number=54,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=257,
    abilities=[
        Attack(
            title="Fist of Focus",
            game_text="Attach an Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flare Storm",
            game_text="Flip a coin for each Fire Energy attached to this Pok\u00e9mon. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)