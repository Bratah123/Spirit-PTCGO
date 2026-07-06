from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d78897f-0e8b-5acf-9f68-1c0754d3f50b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianZigzagoon.Name",
    display_name="Galarian Zigzagoon",
    searchable_by=["Galarian Zigzagoon", "Basic", "GalarianZigzagoon"],
    subtypes=["Basic"],
    collector_number=159,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=263,
    abilities=[
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)