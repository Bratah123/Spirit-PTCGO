from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import EffectContext

async def worker(ctx: EffectContext):
    await ctx.draw_cards(3)
    await ctx.discard_stadium()

card = SupporterCardDef(
    guid="dc9fdbc1-755c-5e32-a87a-bbf13a4923af",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Worker.Name",
    display_name="Worker",
    searchable_by=["Worker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SWSH12",
    rarity=Rarities.RareRainbow,
    effect=worker
)
