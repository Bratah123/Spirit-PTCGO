"""STUB: effect not implemented — do not guess mechanics.
Gallade-EX (Promo_XY #XY45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="98c2c863-0bd6-5297-82d4-ec1354a1a43f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name",
    display_name="Gallade-EX",
    searchable_by=["Gallade-EX", "Basic", "EX", "GalladeEX"],
    subtypes=["Basic", "EX"],
    collector_number=45,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Assault Sword",
            game_text="If your opponent's Active Pok\u00e9mon has no Energy attached to it, this attack does 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Cross Slash",
            game_text="This Pok\u00e9mon can't use Cross Slash during your next turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)