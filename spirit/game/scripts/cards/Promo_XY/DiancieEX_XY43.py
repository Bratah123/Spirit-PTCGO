"""STUB: effect not implemented — do not guess mechanics.
Diancie-EX (Promo_XY #XY43): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e3d3f361-cacc-54d1-8dcb-bc2f4e6e962d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name",
    display_name="Diancie-EX",
    searchable_by=["Diancie-EX", "Basic", "EX", "DiancieEX"],
    subtypes=["Basic", "EX"],
    collector_number=43,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=719,
    abilities=[
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Luminous Swirl",
            game_text="Flip 2 coins. This attack does 40 more damage for each heads.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)