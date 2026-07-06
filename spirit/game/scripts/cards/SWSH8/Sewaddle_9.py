from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="815eebbc-d71a-53a9-bc69-78595e5d0082",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    display_name="Sewaddle",
    searchable_by=["Sewaddle", "Basic", "Sewaddle"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SWSH8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=540,
    abilities=[
        Attack(
            title="Grass Munch",
            game_text="Discard a Grass Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)