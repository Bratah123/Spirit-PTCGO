from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5f1e43c0-1512-5a39-a9ff-bbb84c999e47",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic", "Cubone"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=104,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)