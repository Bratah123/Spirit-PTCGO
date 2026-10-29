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
    guid="23852def-8394-50f6-8c0f-aab0f1734a11",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    display_name="Natu",
    searchable_by=["Natu", "Basic", "Natu"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=177,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=future_sight,
        ),
    ],
)