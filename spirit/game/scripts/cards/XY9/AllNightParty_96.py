from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES


def all_night_party_condition(board, player_id, stadium=None):
    a = board.active_pokemon(player_id)
    return a is not None and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP] in \
        (a.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


async def all_night_party(ctx):
    """If your Active Pokemon is Asleep, remove that Special Condition and heal 30 damage from it."""
    a = ctx.my_active()
    if a is None:
        return
    await ctx.cure_condition(a, SpecialConditions.ASLEEP)
    await ctx.heal(30, a)


card = StadiumCardDef(
    guid="06cda8ff-46cf-5b60-8302-9eab2e539f61",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AllNightParty.Name",
    display_name="All-Night Party",
    searchable_by=["All-Night Party", "Stadium"],
    subtypes=["Stadium"],
    collector_number=96,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="All-Night Party",
        game_text="Once during each player's turn, if that player's Active Pok\u00e9mon is Asleep, he or she may remove that Special Condition and heal 30 damage from that Pok\u00e9mon.",
        activation=Activations.ONCE_PER_TURN,
        condition=all_night_party_condition,
        effect=all_night_party,
    )
)
