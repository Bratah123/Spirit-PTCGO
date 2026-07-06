from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c5ab83e-4f17-5be2-a68f-a5442fa0ff3d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name",
    display_name="Cufant",
    searchable_by=["Cufant", "Basic", "Cufant"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SWSH1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=878,
    abilities=[
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)