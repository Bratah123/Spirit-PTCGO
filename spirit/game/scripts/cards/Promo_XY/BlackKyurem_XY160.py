"""STUB: effect not implemented — do not guess mechanics.
Black Kyurem (Promo_XY #XY160): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e77c48f4-aa04-5e64-8fec-632fab591288",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyurem.Name",
    display_name="Black Kyurem",
    searchable_by=["Black Kyurem", "Basic", "BlackKyurem"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Frosty Thunder",
            game_text="If this Pok\u00e9mon has any Lightning Energy attached to it, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)