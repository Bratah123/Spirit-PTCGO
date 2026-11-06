from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import TurnDamageModifier


async def iris(ctx):
    """During this turn, your Pokemon's attacks do 10 more damage to the
    Active Pokemon for each Prize card your opponent has taken (before W/R)."""
    taken = ctx.prizes_taken(ctx.opponent_id)
    if taken > 0:
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            amount=10 * taken, player_id=ctx.player_id, opposing_active_only=True))


card = SupporterCardDef(
    guid="6c18a227-5400-5a2d-b108-4713a501d512",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iris.Name",
    display_name="Iris",
    searchable_by=["Iris", "Supporter"],
    subtypes=["Supporter"],
    collector_number=81,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=iris
)
