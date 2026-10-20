from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import is_basic_energy_card


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def _basic_energy_in_discard(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else []) if is_basic_energy_card(c)]


def team_aqua_admin_condition(board, player_id):
    a = board.active_pokemon(player_id)
    return a is not None and _team(a, "Aqua") and bool(_basic_energy_in_discard(board, player_id))


async def team_aqua_admin(ctx):
    """Attach a basic Energy card from your discard pile to your Active Team Aqua Pokemon."""
    a = ctx.my_active()
    pool = _basic_energy_in_discard(ctx.board, ctx.player_id)
    if a is None or not pool or not _team(a, "Aqua"):
        return
    pick = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a basic Energy to attach")
    if pick:
        await ctx.attach_energy(pick[0], a)


card = SupporterCardDef(
    guid="6d4713e6-8061-5b33-b82b-7c09ba157c49",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaAdmin.Name",
    display_name="Team Aqua Admin",
    searchable_by=["Team Aqua Admin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=25,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    condition=team_aqua_admin_condition,
    effect=team_aqua_admin
)
