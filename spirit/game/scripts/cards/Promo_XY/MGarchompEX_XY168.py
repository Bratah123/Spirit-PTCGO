"""STUB: effect not implemented — do not guess mechanics.
M Garchomp-EX (Promo_XY #XY168): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="280886af-32ed-5595-9cb8-54ebe102ad14",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGarchompEX.Name",
    display_name="M Garchomp-EX",
    searchable_by=["M Garchomp-EX", "MEGA", "EX", "MGarchompEX"],
    subtypes=["MEGA", "EX"],
    collector_number=168,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompEX.Name",
    family_id=445,
    abilities=[
        Attack(
            title="Crimson Edge",
            game_text="This Pok\u00e9mon does 10 damage to itself for each damage counter on it.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)