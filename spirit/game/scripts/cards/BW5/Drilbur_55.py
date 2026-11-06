from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f9a3217-405e-5af0-a7da-034a8881e13b",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BW5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=529,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)