from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _present(ctx):
    """Flip a coin. If heads, search your deck for a card and put it into your hand; shuffle."""
    results = await ctx.flip_coins(1, "Present")
    if not results or not results[0]:
        return
    picks = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put into your hand.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="db78afed-6d11-530e-b144-e5adb6f0e400",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabebe.Name",
    display_name="Flab\u00e9b\u00e9",
    searchable_by=["Flabébé", "Basic", "Flabebe"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Attack(
            title="Wish",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_present,
        ),
    ],
)