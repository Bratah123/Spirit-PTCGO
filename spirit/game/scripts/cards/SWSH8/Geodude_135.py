from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cbfa344f-3d1b-5522-884c-5c666c0f1faf",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    display_name="Geodude",
    searchable_by=["Geodude", "Basic", "Geodude"],
    subtypes=["Basic"],
    collector_number=135,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=74,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)