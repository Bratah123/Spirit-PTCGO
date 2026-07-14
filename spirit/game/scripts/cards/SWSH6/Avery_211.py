from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import full_stack


async def avery(ctx):
    drawn = await ctx.draw_cards(3)
    if not drawn:
        return
    while len(ctx.opponent_bench()) > 3:
        bench = ctx.opponent_bench()
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to discard", player_id=ctx.opponent_id
        )
        if target is None:
            break
        await ctx.discard_cards(full_stack(target))


card = SupporterCardDef(
    guid="f5c2122f-e807-5e14-857f-bdbb7f24364d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Avery.Name",
    display_name="Avery",
    searchable_by=["Avery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=211,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    effect=avery,
)
