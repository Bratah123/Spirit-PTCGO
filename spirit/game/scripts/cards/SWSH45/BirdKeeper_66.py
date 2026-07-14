from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench


async def bird_keeper(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon. If you do, draw 3 cards."""
    target = await ctx.choose_pokemon(ctx.my_bench(), "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="82d01bbf-c787-595d-8d14-6afce683a65d",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BirdKeeper.Name",
    display_name="Bird Keeper",
    searchable_by=["Bird Keeper", "Supporter"],
    subtypes=["Supporter"],
    collector_number=66,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=bird_keeper,
    condition=player_has_bench
)
