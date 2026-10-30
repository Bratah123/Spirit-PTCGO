from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77a22dae-b170-5c60-8738-4a28b6c439d0",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonchan.Name",
    display_name="Hitmonchan",
    searchable_by=["Hitmonchan", "Basic", "Hitmonchan"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=107,
    abilities=[
        Attack(
            title="Jab",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Special Punch",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)