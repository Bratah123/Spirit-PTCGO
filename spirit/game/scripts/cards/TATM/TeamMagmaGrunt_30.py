from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def team_magma_grunt_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and len(hand.children) >= 2)


async def team_magma_grunt(ctx):
    """Discard a card from your hand; draw 3 cards (+1 if you discarded a Team Magma Pokemon)."""
    gone = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card")
    if not gone:
        return
    bonus = 1 if is_pokemon_card(gone[0]) and _team(gone[0], "Magma") else 0
    await ctx.draw_cards(3 + bonus)


card = SupporterCardDef(
    guid="b70f88dd-ba84-5684-9ca6-03162b5b6181",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaGrunt.Name",
    display_name="Team Magma Grunt",
    searchable_by=["Team Magma Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=30,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    condition=team_magma_grunt_condition,
    effect=team_magma_grunt
)
