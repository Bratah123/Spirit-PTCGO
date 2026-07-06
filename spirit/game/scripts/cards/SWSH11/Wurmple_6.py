from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="86568dbe-e9ff-5434-ac85-21555ae5f63d",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic", "Wurmple"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Attack(
            title="Sting",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Creepy-Crawly Congregation",
            game_text="Search your deck for any number of Wurmple, Silcoon, Beautifly, Cascoon, and Dustox, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 3},
            effect=unimplemented,
        ),
    ],
)