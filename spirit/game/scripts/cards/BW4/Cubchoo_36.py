from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9b1be01-eb6d-5106-9603-7ecb0904be43",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo", "Basic", "Cubchoo"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=613,
    abilities=[
        Attack(
            title="Sniffle",
            game_text="During your next turn, this Pok\u00e9mon's Belt attack's base damage is 40.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Belt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)