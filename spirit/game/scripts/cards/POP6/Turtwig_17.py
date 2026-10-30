from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8abd329c-fb75-5676-884b-864ff7eaf08c",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="POP6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=387,
    abilities=[
        Attack(
            title="Tackle",
            cost={},
            damage=10,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)