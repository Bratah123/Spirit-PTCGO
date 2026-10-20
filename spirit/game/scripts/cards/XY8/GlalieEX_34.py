"""STUB: effect not implemented — do not guess mechanics.
Glalie-EX (XY8 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4ec81b5a-a313-56d3-b66a-ab18c0244793",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlalieEX.Name",
    display_name="Glalie-EX",
    searchable_by=["Glalie-EX", "Basic", "EX", "GlalieEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="XY8",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=362,
    abilities=[
        Attack(
            title="Ice Breath",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Instant Freeze",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)