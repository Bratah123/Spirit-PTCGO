from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def team_aqua_grunt_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and len(hand.children) >= 2)


async def team_aqua_grunt(ctx):
    """Discard a card from your hand; draw 3 cards (+1 if you discarded a Team Aqua Pokemon)."""
    gone = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card")
    if not gone:
        return
    bonus = 1 if is_pokemon_card(gone[0]) and _team(gone[0], "Aqua") else 0
    await ctx.draw_cards(3 + bonus)


card = SupporterCardDef(
    guid="8f7dd117-d369-5ae5-8de7-598a8da25c9c",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaGrunt.Name",
    display_name="Team Aqua Grunt",
    searchable_by=["Team Aqua Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    condition=team_aqua_grunt_condition,
    effect=team_aqua_grunt
)
