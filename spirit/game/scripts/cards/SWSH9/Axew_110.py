from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b2c9db6f-0a37-5c13-b147-5124b8e49527",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=610,
    abilities=[
        Attack(
            title="Ultra Evolution",
            game_text="Flip a coin. If heads, search your deck for a Haxorus and put it onto this Axew to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)