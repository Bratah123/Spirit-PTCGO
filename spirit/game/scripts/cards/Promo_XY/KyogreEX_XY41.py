"""STUB: effect not implemented — do not guess mechanics.
Kyogre-EX (Promo_XY #XY41): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf3ae6aa-39c3-5ff9-8444-8706fc5e1f75",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name",
    display_name="Kyogre-EX",
    searchable_by=["Kyogre-EX", "Basic", "EX", "KyogreEX"],
    subtypes=["Basic", "EX"],
    collector_number=41,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giant Whirlpool",
            game_text="Return 2 Water Energy attached to this Pok\u00e9mon to your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)