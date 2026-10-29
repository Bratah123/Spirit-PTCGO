from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_evolution_pokemon
from spirit.game.card_effects.trainers import deck_nonempty


async def _timer_ball(ctx):
    """Flip 2 coins. For each heads, search your deck for an Evolution Pokemon; shuffle."""
    results = await ctx.flip_coins(2, "Timer Ball")
    heads = sum(1 for r in results or [] if r)
    if heads:
        picks = await ctx.search_deck(is_evolution_pokemon, count=heads, minimum=0,
                                      prompt=f"Choose up to {heads} Evolution Pokémon.")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()


card = ItemCardDef(
    guid="4b3ceeb2-1e9f-50b9-b82f-7a3c962117a3",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimerBall.Name",
    display_name="Timer Ball",
    searchable_by=["Timer Ball", "Item"],
    subtypes=["Item"],
    collector_number=134,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_timer_ball,
    condition=deck_nonempty
)
