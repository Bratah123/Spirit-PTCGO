"""STUB: effect not implemented — do not guess mechanics.
Houndoom-EX (XY8 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c6c9d67c-848a-5637-97da-8f8878c1e741",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomEX.Name",
    display_name="Houndoom-EX",
    searchable_by=["Houndoom-EX", "Basic", "EX", "HoundoomEX"],
    subtypes=["Basic", "EX"],
    collector_number=21,
    set_code="XY8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=229,
    abilities=[
        Attack(
            title="Melting Horn",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Grand Flame",
            game_text="Attach a Fire Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)