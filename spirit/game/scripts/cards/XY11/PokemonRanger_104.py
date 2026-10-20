from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def pokemon_ranger(ctx):
    """Remove all effects of attacks on each player and their Pokemon.
    Approximation: clears attack/retreat/attach locks, coin-gate checks, play
    locks and temporary passives (on Pokemon and player-wide); Special
    Conditions and damage counters stay."""
    state = ctx.session.turn_state
    ids = {p.entity_id for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()}
    for key in [k for k in state.attack_locks if k[0] in ids]:
        state.attack_locks.pop(key, None)
    for eid in ids:
        state.retreat_locks.pop(eid, None)
        state.attach_restrictions.pop(eid, None)
        state.attack_flip_checks.pop(eid, None)
    state.play_locks.clear()
    hands = {a.entity_id for a in (ctx.board.find_player_area(pid, "hand") for pid in (ctx.player_id, ctx.opponent_id)) if a}
    ctx.board.temporary_passives = [
        tp for tp in (getattr(ctx.board, "temporary_passives", None) or [])
        if tp.carrier_entity_id not in ids and tp.carrier_entity_id not in hands
    ]


card = SupporterCardDef(
    guid="9f6fdde7-2978-541e-aa87-e53eb07019ce",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRanger.Name",
    display_name="Pok\u00e9mon Ranger",
    searchable_by=["Pokémon Ranger", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    effect=pokemon_ranger
)
