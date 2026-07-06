from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f74c1ce2-1da1-5af1-8b2f-4a18da88c2a0",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name",
    display_name="Togedemaru",
    searchable_by=["Togedemaru", "Basic", "Togedemaru"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=777,
    abilities=[
        Attack(
            title="Toge Dash",
            game_text="Flip a coin. If heads, during your opponent's next turn, if this Pok\u00e9mon is Knocked Out, your opponent can't take any Prize cards for it.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)