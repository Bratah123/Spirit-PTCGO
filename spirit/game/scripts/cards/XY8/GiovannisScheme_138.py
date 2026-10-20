from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier


async def giovannis_scheme(ctx):
    """Choose 1: draw until you have 5 cards in hand; or this turn your
    Pokemon's attacks do 20 more damage to the opponent's Active."""
    pick = await ctx.choose("Giovanni's Scheme", ["Draw until 5 cards", "+20 damage this turn"])
    if pick == 0:
        await ctx.draw_until(5)
    else:
        ctx.add_turn_damage_modifier(TurnDamageModifier(20, ctx.player_id))


card = SupporterCardDef(
    guid="df0f98f9-b058-544a-a2dd-c5f71f3f3f5f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisScheme.Name",
    display_name="Giovanni's Scheme",
    searchable_by=["Giovanni's Scheme", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=giovannis_scheme
)
