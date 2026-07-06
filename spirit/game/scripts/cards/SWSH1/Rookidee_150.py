from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="877b454d-98a1-5f1d-8cb6-54f6680b7d23",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    display_name="Rookidee",
    searchable_by=["Rookidee", "Basic", "Rookidee"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=821,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)