from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="61f7538e-0343-5e55-a014-05cd4d6379b9",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    display_name="Shroomish",
    searchable_by=["Shroomish", "Basic", "Shroomish"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="XY3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=285,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)