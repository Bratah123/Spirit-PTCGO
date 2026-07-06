from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e279b9fa-049b-52de-9515-5cb7354cae9d",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    display_name="Wooper",
    searchable_by=["Wooper", "Basic", "Wooper"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=194,
    abilities=[
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)