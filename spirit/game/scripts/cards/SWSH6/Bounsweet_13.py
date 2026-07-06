from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b6bc046-6694-54d0-96dd-6aa86d133922",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    display_name="Bounsweet",
    searchable_by=["Bounsweet", "Basic", "Bounsweet"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=761,
    abilities=[
        Attack(
            title="Splash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)