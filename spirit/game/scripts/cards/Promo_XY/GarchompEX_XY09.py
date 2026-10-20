"""STUB: effect not implemented — do not guess mechanics.
Garchomp-EX (Promo_XY #XY09): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="849da797-6d6b-5fad-bdf7-b406a6701921",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompEX.Name",
    display_name="Garchomp-EX",
    searchable_by=["Garchomp-EX", "Basic", "EX", "GarchompEX"],
    subtypes=["Basic", "EX"],
    collector_number=9,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Dual Chop",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)