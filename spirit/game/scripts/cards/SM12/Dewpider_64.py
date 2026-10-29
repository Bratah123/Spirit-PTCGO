from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4740c87a-b8b2-5bea-bcec-84bd6c887c48",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    display_name="Dewpider",
    searchable_by=["Dewpider", "Basic", "Dewpider"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=751,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)