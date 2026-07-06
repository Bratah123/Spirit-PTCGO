from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="299711ab-ea84-5f49-a104-92a0e5f69587",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    display_name="Chewtle",
    searchable_by=["Chewtle", "Basic", "Chewtle"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=833,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)