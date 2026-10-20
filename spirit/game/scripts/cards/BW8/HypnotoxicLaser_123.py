from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, SpecialConditions


def _opponent_has_active(board, player_id):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    return opponent is not None and board.active_pokemon(opponent) is not None


async def hypnotoxic_laser(ctx):
    """Your opponent's Active Pokemon is now Poisoned. Flip a coin; if heads
    it is also Asleep."""
    target = ctx.opponent_active()
    if target is None:
        return
    await ctx.apply_special_condition(target, SpecialConditions.POISONED)
    results = await ctx.flip_coins(1, "Hypnotoxic Laser")
    if results and results[0]:
        await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


card = ItemCardDef(
    guid="56651494-fb94-5b38-9de7-64e8845b5336",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HypnotoxicLaser.Name",
    display_name="Hypnotoxic Laser",
    searchable_by=["Hypnotoxic Laser", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=123,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=hypnotoxic_laser,
    condition=_opponent_has_active
)
