"""STUB: effect not implemented — do not guess mechanics.
Shellos West Sea (DP3 #107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e784acf-4028-5b6c-83ea-f736d304b6a2",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosWestSea.Name",
    display_name="Shellos West Sea",
    searchable_by=["Shellos West Sea", "Basic", "ShellosWestSea"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=422,
    abilities=[
        Attack(
            title="Mud Spatter",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Recover",
            game_text="Discard a Water Energy attached to Shellos West Sea and remove all damage counters from Shellos West Sea.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)