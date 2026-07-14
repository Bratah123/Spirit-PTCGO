from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def branch_calculation(ctx):
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
    guid="efa4694c-67df-5fcb-aee3-9f4adfba1a1a",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic", "Porygon"],
    subtypes=["Basic"],
    collector_number=140,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Branch Calculation",
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=branch_calculation,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
