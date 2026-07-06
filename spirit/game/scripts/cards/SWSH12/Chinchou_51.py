from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b947e8ff-72cf-551b-84b3-b7aa9fd32076",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic", "Chinchou"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=170,
    abilities=[
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=20,
        ),
    ],
)