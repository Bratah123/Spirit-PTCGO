from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ce4a0c8d-9f0f-5848-979a-46ff0a40d69e",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Wild Freeze",
            game_text="This Pok\u00e9mon also does 50 damage to itself. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)