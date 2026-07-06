from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7b64717-c408-5076-b063-da0602af7dcb",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    display_name="Rillaboom V",
    searchable_by=["Rillaboom V", "Basic", "V", "RillaboomV"],
    subtypes=["Basic", "V"],
    collector_number=17,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=812,
    abilities=[
        Attack(
            title="Forest Feast",
            game_text="Search your deck for up to 2 Basic Grass Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Wood Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=unimplemented,
        ),
    ],
)