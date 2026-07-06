from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="830c1e0d-501d-58cd-b785-48ad288110a9",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic", "Gible"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=443,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)