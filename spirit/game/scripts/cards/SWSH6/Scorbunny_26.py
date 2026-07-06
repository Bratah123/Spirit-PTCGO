from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23e3c909-0afc-58da-874a-9fa5c3a26fe8",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    display_name="Scorbunny",
    searchable_by=["Scorbunny", "Basic", "Single Strike", "Scorbunny"],
    subtypes=["Basic", "Single Strike"],
    collector_number=26,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=813,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)