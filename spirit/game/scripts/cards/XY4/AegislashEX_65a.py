"""STUB: effect not implemented — do not guess mechanics.
Aegislash-EX (XY4 #65a): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43f6013a-4084-5522-8d9c-2d523664a78b",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AegislashEX.Name",
    display_name="Aegislash-EX",
    searchable_by=["Aegislash-EX", "Basic", "EX", "AegislashEX"],
    subtypes=["Basic", "EX"],
    collector_number=124,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=681,
    abilities=[
        Ability(
            title="Mighty Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from each of your opponent's Pok\u00e9mon that has Special Energy attached to it.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Slash Blast",
            game_text="This attack does 20 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)