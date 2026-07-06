from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c92919b-3dcf-55b8-866f-daa63bc46076",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    display_name="Galarian Meowth",
    searchable_by=["Galarian Meowth", "Basic", "GalarianMeowth"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=52,
    abilities=[
        Ability(
            title="Evolution Roar",
            game_text="You must discard 2 cards from your hand in order to use this Ability. Once during your turn, you may search your deck for a Galarian Perrserker, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)