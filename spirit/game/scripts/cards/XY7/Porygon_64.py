from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _data_check(ctx):
    """Look through your deck. Shuffle your deck afterward."""
    deck = list(reversed(ctx.deck()))
    if deck:
        await ctx.choose_cards(deck, 1, minimum=0, display_cards=deck, prompt="Your deck")
        await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="42d15757-0ad3-5d95-b541-a845fb6279ab",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Data Check",
            game_text="Look through your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_data_check,
        ),
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)