from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def nasty_plot(ctx):
    """Search deck for a card and put it into your hand."""
    picks = await ctx.search_deck(
        count=1, minimum=1,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="1e3aba23-2d6d-57e0-994b-5bdcb2ebc8cd",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    display_name="Zorua",
    searchable_by=["Zorua", "Basic", "Zorua"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=nasty_plot,
        ),
    ],
)