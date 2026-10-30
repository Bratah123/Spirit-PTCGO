"""STUB: effect not implemented — do not guess mechanics.
Shellos East Sea (DP3 #106): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="adfb3397-2f68-5590-acda-0c442c67043f",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosEastSea.Name",
    display_name="Shellos East Sea",
    searchable_by=["Shellos East Sea", "Basic", "ShellosEastSea"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=422,
    abilities=[
        Attack(
            title="Shell Hunting",
            game_text="Search your deck for up to 2 in any combination of Shellos West Sea and Shellos East Sea and put them on your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sprinkle Water",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)