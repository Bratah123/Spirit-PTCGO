from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def future_sight(ctx):
    """Look at the top 4 cards of either player's deck, put back in any order."""
    choice = await ctx.choose(
        "Look at the top 4 cards of which deck?",
        ["Your deck", "Opponent's deck"], use_panel=False,
    )
    target_pid = ctx.player_id if choice == 0 else ctx.opponent_id
    top = ctx.deck_top(4, target_pid)
    if len(top) <= 1:
        return
    order = await ctx.choose_cards(
        top, len(top), minimum=len(top), ordered=True, player_id=ctx.player_id,
        prompt="Put the cards back in any order",
    )
    if not order:
        order = top
    deck = ctx.board.find_player_area(target_pid, "deck")
    for card in order:
        if card in deck.children:
            deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)


card = PokemonCardDef(
    guid="4fc8bdeb-2538-5d6a-b8a1-f93ec9f94e71",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic", "Munna"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=517,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=future_sight,
        ),
    ],
)