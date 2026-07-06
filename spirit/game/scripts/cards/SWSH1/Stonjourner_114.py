from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3fae7c1-d3d7-5147-98c0-07d7d6b75eed",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stonjourner.Name",
    display_name="Stonjourner",
    searchable_by=["Stonjourner", "Basic", "Stonjourner"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=874,
    abilities=[
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)