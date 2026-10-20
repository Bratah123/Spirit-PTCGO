from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e651831-0402-5a2a-a67a-73119a2ae47f",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    display_name="Makuhita",
    searchable_by=["Makuhita", "Basic", "Makuhita"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=296,
    abilities=[
        Attack(
            title="Punch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Strength",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)