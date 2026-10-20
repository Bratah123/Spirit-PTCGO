from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card


async def fang_snipe(ctx):
    """30 damage. Opponent reveals their hand; discard a Trainer card found there."""
    await ctx.deal_damage()
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    matches = [c for c in hand if is_trainer_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, minimum=1,
        prompt="Choose a Trainer card to discard from your opponent's hand.",
        display_cards=hand,
    )
    await ctx.discard_cards(picks)


async def _future_sight(ctx):
    """Look at the top 5 cards of either player's deck and put them back in any order."""
    pid = ctx.opponent_id if await ctx.ask_yes_no("Look at your opponent's deck? (No = your own)") else ctx.player_id
    top = ctx.deck_top(5, pid)
    if not top:
        return
    order = await ctx.choose_cards(top, len(top), minimum=len(top), ordered=True, display_cards=top,
                                   prompt="Choose the order (first = top)") or top
    for card in reversed(list(order)):
        await ctx.put_on_top_of_deck(card)


card = PokemonCardDef(
    guid="f868d04d-e989-5dc5-bbf7-bb2d6d5603aa",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 5 cards of either player's deck and put them back on top of that player's deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_future_sight,
        ),
        Attack(
            title="Stressful Eye",
            game_text="Your opponent reveals his or her hand. Discard a Trainer card you find there.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=fang_snipe,
        ),
    ],
)