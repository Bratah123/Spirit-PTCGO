"""STUB: effect not implemented — do not guess mechanics.
Steelix-EX (XY11 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="89cd170e-8425-55d0-aa48-67c9c5fe92a0",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SteelixEX.Name",
    display_name="Steelix-EX",
    searchable_by=["Steelix-EX", "Basic", "EX", "SteelixEX"],
    subtypes=["Basic", "EX"],
    collector_number=108,
    set_code="XY11",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=208,
    abilities=[
        Attack(
            title="Wild Edge",
            game_text="You may do 50 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 100 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)