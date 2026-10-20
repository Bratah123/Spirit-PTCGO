from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _fiddle_around(ctx):
    """Look at the top 3 cards of your opponent's deck and put them back in any order."""
    if ctx.deck(ctx.opponent_id):
        await ctx.reorder_deck_top(3, player_id=ctx.opponent_id,
                                   prompt="Rearrange the top of your opponent's deck")


card = PokemonCardDef(
    guid="4a120da5-b852-5cae-a42b-321b8789025d",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Fiddle Around",
            game_text="Look at the top 3 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_fiddle_around,
        ),
        Attack(
            title="Tail Jab",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)