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


from spirit.game.card_effects.pokemon import delayed_knockout


async def doom_news(ctx):
    """Return attached Energy to hand, then delayed KO on the Defending Pokémon."""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies:
        await ctx.put_in_hand(energies, reveal=False)
    await delayed_knockout(ctx)


card = PokemonCardDef(
    guid="09b0e8fc-e7f4-5a79-b480-80f4dbc79a82",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=future_sight,
        ),
        Attack(
            title="Doom News",
            game_text="Put all Energy attached to this Pok\u00e9mon into your hand. At the end of your opponent's next turn, the Defending Pok\u00e9mon will be Knocked Out.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=doom_news,
        ),
    ],
)