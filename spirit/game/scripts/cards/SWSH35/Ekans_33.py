from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c30350ea-d25e-5b07-9017-7a5ec06784c0",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans",
    searchable_by=["Ekans", "Basic", "Ekans"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SWSH35",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=23,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tail Snap",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)