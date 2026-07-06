from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc46f911-8081-5ffe-a712-08b5fcc2d194",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    display_name="Yamper",
    searchable_by=["Yamper", "Basic", "Yamper"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=835,
    abilities=[
        Ability(
            title="Ball Search",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put a Pok\u00e9 Ball card, a Great Ball card, or 1 of each from your discard pile into your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)