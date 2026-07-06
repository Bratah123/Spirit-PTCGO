from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b8927a2-9650-5a0a-9ca7-b010ba01f11c",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    display_name="Nickit",
    searchable_by=["Nickit", "Basic", "Nickit"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=827,
    abilities=[
        Attack(
            title="Tail Whip",
            game_text="Flip a coin. If heads, during your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)