from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities, SpecialConditions
from spirit.game.session.passives import Passive


# stadium entity_id -> player whose Pokemon can't be Confused or Poisoned
# (the other end of the card points at the other player: can't be Asleep or Paralyzed).
_FACING = {}
_CONF_POIS = (SpecialConditions.CONFUSED, SpecialConditions.POISONED)
_SLEEP_PARA = (SpecialConditions.ASLEEP, SpecialConditions.PARALYZED)


def _blocked_for(player_id, stadium_id):
    conf = _FACING.get(stadium_id)
    if conf is None:
        return ()
    return _CONF_POIS if player_id == conf else _SLEEP_PARA


async def chaos_tower_facing(ctx):
    """Choose which way this card faces before you play it; remove the
    newly-prevented Special Conditions already in play."""
    pick = await ctx.choose("Chaos Tower", [
        "Your Pok\u00e9mon can't be Confused or Poisoned; your opponent's can't be Asleep or Paralyzed",
        "Your Pok\u00e9mon can't be Asleep or Paralyzed; your opponent's can't be Confused or Poisoned",
    ], use_panel=False)
    _FACING[ctx.source.entity_id] = ctx.player_id if pick == 0 else ctx.opponent_id
    for pid in (ctx.player_id, ctx.opponent_id):
        for p in ctx.board.pokemon_in_play(pid):
            for cond in _blocked_for(pid, ctx.source.entity_id):
                await ctx.cure_condition(p, cond)


class _ChaosTower(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        return condition in _blocked_for(target.owning_player_id, carrier.entity_id)


card = StadiumCardDef(
    guid="b261ac6f-3f12-5fb5-ac4d-21f93dfe979d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaosTower.Name",
    display_name="Chaos Tower",
    searchable_by=["Chaos Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=_ChaosTower(),
    abilities=[
        Ability(
            title="Chaos Tower",
            game_text="Choose which way this card faces before you play it.",
            trigger=Triggers.ON_PLAY,
            effect=chaos_tower_facing,
        ),
    ]
)
