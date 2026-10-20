from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc05322e-c7fa-51c8-a7aa-13923f91e089",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name",
    display_name="Pansage",
    searchable_by=["Pansage", "Basic", "Pansage"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="BW4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=511,
    abilities=[
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)