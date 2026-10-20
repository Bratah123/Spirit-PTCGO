from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


async def _multiply(ctx):
    """Search your deck for Weedle and put it onto your Bench. Shuffle."""
    bench = ctx.board.find_player_area(ctx.player_id, "bench")
    if bench is not None and len(bench.children) < effective_bench_capacity(ctx.board, ctx.player_id):
        picks = await ctx.search_deck(
            lambda c: is_pokemon_card(c) and getattr(def_for(c.archetype_id), "display_name", None) == "Weedle",
            count=1, minimum=0, prompt="Choose a Weedle")
        for card in picks or []:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="046aa0b1-69ff-5b36-adb2-12d328132300",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="XY5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Multiply",
            game_text="Search your deck for Weedle and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=_multiply,
        ),
    ],
)