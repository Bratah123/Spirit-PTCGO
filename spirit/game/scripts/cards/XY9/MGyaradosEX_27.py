"""STUB: effect not implemented — do not guess mechanics.
M Gyarados-EX (XY9 #27): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edce07d9-2384-5316-b5f5-44e4430a43f0",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGyaradosEX.Name",
    display_name="M Gyarados-EX",
    searchable_by=["M Gyarados-EX", "MEGA", "EX", "MGyaradosEX"],
    subtypes=["MEGA", "EX"],
    collector_number=27,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosEX.Name",
    family_id=130,
    abilities=[
        Attack(
            title="Blast Geyser",
            game_text="You may do 20 more damage for each Water Energy attached to this Pok\u00e9mon. If you do, discard the top 2 cards of your deck.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)