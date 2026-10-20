"""STUB: effect not implemented — do not guess mechanics.
Hoopa (Promo_XY #XY90): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83338d69-3f72-59c7-9403-0f795cea3be9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopa.Name",
    display_name="Hoopa",
    searchable_by=["Hoopa", "Basic", "Hoopa"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Attack(
            title="Summoning Draw",
            game_text="If Pikachu is on your Bench, draw 3 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)