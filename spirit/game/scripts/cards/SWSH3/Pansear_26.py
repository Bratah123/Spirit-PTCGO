from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e71d3bbb-ef0a-5533-b65f-45dce193e244",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    display_name="Pansear",
    searchable_by=["Pansear", "Basic", "Pansear"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=513,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)