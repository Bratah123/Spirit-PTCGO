"""STUB: effect not implemented — do not guess mechanics.
Camerupt-EX (XY5 #146): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eb21cfba-a7f5-55f2-97e8-811f12c6328c",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CameruptEX.Name",
    display_name="Camerupt-EX",
    searchable_by=["Camerupt-EX", "Basic", "EX", "CameruptEX"],
    subtypes=["Basic", "EX"],
    collector_number=146,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=323,
    abilities=[
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Explosive Jet",
            game_text="Discard as many Fire Energy attached to your Pok\u00e9mon as you like. This attack does 50 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)