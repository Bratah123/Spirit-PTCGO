from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6133849a-48e1-5a00-a98f-be3c9454b79d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel",
    searchable_by=["Seel", "Basic", "Seel"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)