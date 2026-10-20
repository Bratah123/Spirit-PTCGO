from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8c8b31d1-6956-5fb8-9a89-29f9509ad666",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name",
    display_name="Vanillite",
    searchable_by=["Vanillite", "Basic", "Vanillite"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=582,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)