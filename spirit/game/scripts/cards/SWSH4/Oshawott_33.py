from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3685e193-4ec8-5eff-8135-24fe6196ab75",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    display_name="Oshawott",
    searchable_by=["Oshawott", "Basic", "Oshawott"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=501,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Seashell Attack",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)