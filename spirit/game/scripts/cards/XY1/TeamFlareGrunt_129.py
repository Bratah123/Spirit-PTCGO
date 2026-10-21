from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card


def team_flare_grunt_condition(board, player_id):
    """Your opponent's Active Pokemon has Energy attached."""
    opp = next((p for p in board.player_ids if p != player_id), None)
    area = board.find_player_area(opp, "activePokemonArea") if opp else None
    active = area.children[0] if area is not None and area.children else None
    return active is not None and any(is_energy_card(c) for c in active.children)


async def team_flare_grunt(ctx):
    """Discard an Energy attached to your opponent's Active Pokemon."""
    target = ctx.opponent_active()
    if target is None or not ctx.attached_energies(target):
        return
    await ctx.discard_energy_from(target, 1, minimum=1, prompt="Choose an Energy to discard")


card = SupporterCardDef(
    guid="c91261c9-93cc-515f-990f-575006157dfc",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamFlareGrunt.Name",
    display_name="Team Flare Grunt",
    searchable_by=["Team Flare Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=team_flare_grunt,
    condition=team_flare_grunt_condition
)
