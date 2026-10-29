from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e963556b-5cdf-5cf2-b696-1da36f62be11",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    display_name="Cosmog",
    searchable_by=["Cosmog", "Basic", "Cosmog"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=789,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)