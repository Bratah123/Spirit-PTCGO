from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def drone_rotom(ctx):
    """Opponent reveals their hand. Then look at the top card of their deck."""
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    await ctx.present_card_choice(
        top[0], "Top card of your opponent's deck", ["OK"])


card = ItemCardDef(
    guid="67bc7ac0-8aff-5e1c-a677-d7cb85bc72e9",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DroneRotom.Name",
    display_name="Drone Rotom",
    searchable_by=["Drone Rotom", "Item"],
    subtypes=["Item"],
    collector_number=151,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    effect=drone_rotom,
)
