from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for


def _is_mega(p):
    return "MEGA" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def faded_town(ctx):
    """Between turns, put 2 damage counters on each Mega Evolution Pokemon."""
    for pid in (ctx.player_id, ctx.opponent_id):
        for p in list(ctx.board.pokemon_in_play(pid)):
            if _is_mega(p):
                await ctx.place_damage_counters(2, [p])


card = StadiumCardDef(
    guid="7c3fbfb4-e8e8-5fba-aa41-921b5747b179",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FadedTown.Name",
    display_name="Faded Town",
    searchable_by=["Faded Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=73,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Faded Town",
            game_text="At any time between turns, put 2 damage counters on each Mega Evolution Pok\u00e9mon.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=faded_town,
        ),
    ]
)
