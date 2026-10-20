from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def _pool(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return [c for c in (discard.children if discard else []) if is_pokemon_card(c) and _team(c, "Magma")]


def team_magma_admin_condition(board, player_id):
    return bool(_pool(board, player_id))


async def team_magma_admin(ctx):
    """Put up to 3 Team Magma Pokemon from your discard pile into your hand."""
    pool = _pool(ctx.board, ctx.player_id)
    picked = await ctx.choose_cards(pool, min(3, len(pool)), minimum=1, prompt="Choose up to 3 Team Magma Pokémon")
    if picked:
        await ctx.put_in_hand(picked)


card = SupporterCardDef(
    guid="0a9d9923-ad43-56ca-9b2b-e2ffc812c8bc",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaAdmin.Name",
    display_name="Team Magma Admin",
    searchable_by=["Team Magma Admin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=29,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    condition=team_magma_admin_condition,
    effect=team_magma_admin
)
