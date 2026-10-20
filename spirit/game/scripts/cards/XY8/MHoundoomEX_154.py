"""STUB: effect not implemented — do not guess mechanics.
M Houndoom-EX (XY8 #154): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa41bbc5-918f-5aec-8563-775d7239a96d",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MHoundoomEX.Name",
    display_name="M Houndoom-EX",
    searchable_by=["M Houndoom-EX", "MEGA", "EX", "MHoundoomEX"],
    subtypes=["MEGA", "EX"],
    collector_number=154,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HoundoomEX.Name",
    family_id=229,
    abilities=[
        Attack(
            title="Inferno Fang",
            game_text="You may discard all Fire Energy attached to this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2},
            damage=80,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)