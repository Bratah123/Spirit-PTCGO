"""STUB: effect not implemented — do not guess mechanics.
M Glalie-EX (XY8 #35): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26a9e4aa-68c0-5247-9b09-205c7016d12c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGlalieEX.Name",
    display_name="M Glalie-EX",
    searchable_by=["M Glalie-EX", "MEGA", "EX", "MGlalieEX"],
    subtypes=["MEGA", "EX"],
    collector_number=35,
    set_code="XY8",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlalieEX.Name",
    family_id=362,
    abilities=[
        Attack(
            title="Cryo Mouth",
            game_text="If this Pok\u00e9mon has 10 or more damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)