"""STUB: effect not implemented — do not guess mechanics.
Absol-EX (Promo_XY #XY62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23e34891-0992-5ab6-b313-84956259dfa4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AbsolEX.Name",
    display_name="Absol-EX",
    searchable_by=["Absol-EX", "Basic", "EX", "AbsolEX"],
    subtypes=["Basic", "EX"],
    collector_number=62,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Attack(
            title="Dark Fang",
            game_text="Flip a coin. If heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dark Edge",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)