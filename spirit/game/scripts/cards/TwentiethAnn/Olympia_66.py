from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench


async def olympia(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon. If you do, heal
    30 damage from the Pokemon you moved to your Bench."""
    old = ctx.my_active()
    bench = ctx.my_bench()
    if old is None or not bench:
        return
    t = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if t is not None and await ctx.switch_active(ctx.player_id, t):
        await ctx.heal(30, old)


card = SupporterCardDef(
    guid="06a476f5-5dbe-54e5-9687-eeaf9c1f71c5",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olympia.Name",
    display_name="Olympia",
    searchable_by=["Olympia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=66,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    condition=player_has_bench,
    effect=olympia
)
