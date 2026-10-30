from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="455aa418-4cef-519e-b2c8-c651675e7638",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    display_name="Treecko",
    searchable_by=["Treecko", "Basic", "Treecko"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=252,
    abilities=[
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)