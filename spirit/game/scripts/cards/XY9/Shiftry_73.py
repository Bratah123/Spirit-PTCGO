from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card


async def _roll_up(ctx):
    """Flip 3 coins; any heads: opponent reveals their hand; discard a card from it per heads."""
    results = await ctx.flip_coins(3, ctx.ability.title)
    heads = sum(1 for r in results or [] if r)
    hand = list(ctx.hand(ctx.opponent_id))
    if not heads or not hand:
        return
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    n = min(heads, len(hand))
    picks = await ctx.choose_cards(hand, n, minimum=n, display_cards=hand, prompt=f"Discard {n} card(s)")
    if picks:
        await ctx.discard_cards(picks)


async def _otherworldly_return(ctx):
    """60; put a Trainer card from your discard pile into your hand."""
    await ctx.deal_damage()
    trainers = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not trainers:
        return
    picks = await ctx.choose_cards(trainers, 1, minimum=1,
                                   prompt="Choose a Trainer card to put into your hand")
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="6e5b96c8-b6a0-55de-a1f6-bf9cfcb1c659",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Roll Up",
            game_text="Flip 3 coins. If any of them are heads, your opponent reveals his or her hand. Then, for each heads, discard a card from your opponent's hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=_roll_up,
        ),
        Attack(
            title="Otherworldly Return",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_otherworldly_return,
        ),
    ],
)