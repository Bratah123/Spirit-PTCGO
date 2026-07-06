from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7cd86cd1-62e0-5af1-b4c7-208ed4449b12",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    display_name="Skiddo",
    searchable_by=["Skiddo", "Basic", "Skiddo"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=672,
    abilities=[
        Attack(
            title="Synthesis",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)