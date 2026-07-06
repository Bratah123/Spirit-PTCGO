from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f86d0c9b-7034-5b93-bc19-f06cf5e58e10",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=148,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Attack(
            title="Lost Headbutt",
            game_text="Put an Energy attached to your opponent's Active Pok\u00e9mon in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Superpowered Horns",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
        ),
    ],
)