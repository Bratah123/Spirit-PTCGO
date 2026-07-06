from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import EffectContext

async def worker(ctx: EffectContext):
    await ctx.draw_cards(3)
    await ctx.discard_stadium()

card = SupporterCardDef(
    guid="10ee3dce-1772-5b09-b7fb-70aa1c2d6205",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Worker.Name",
    display_name="Worker",
    searchable_by=["Worker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    effect=worker
)
