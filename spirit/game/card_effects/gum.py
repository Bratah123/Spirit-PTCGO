"""Detective Pikachu (GUM) attack and ability behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

from spirit.game.attributes import (
    AttrID, CLIENT_POKEMON_TYPE_NAMES, GameSequence, PokemonTypes,
)
from spirit.game.data_utils import Attack, def_for
from spirit.game.session.legal_actions import attack_cost_satisfied
from spirit.game.session.passives import (
    effective_attack_cost, gx_attacks_blocked,
)
from spirit.game.card_effects.attacks_common import (
    gx_used, self_energy_discard_attack,
)
from spirit.game.card_effects.passives_common import (
    is_in_active_spot, takes_less_passive,
)
from spirit.game.card_effects.support_common import (
    heal_targets, requires_damaged_pokemon,
)


# ======================================================================
# Passives / once-per-turn abilities
# ======================================================================

def _security_guard_protects(target, carrier) -> bool:
    return (
        target.owning_player_id == carrier.owning_player_id
        and is_in_active_spot(carrier)
    )


security_guard_passive = takes_less_passive(30, protects=_security_guard_protects)

table_service = heal_targets(30, "choice")
table_service_condition = requires_damaged_pokemon()


# ======================================================================
# Attacks
# ======================================================================

break_burn = self_energy_discard_attack(count=2, energy_type=PokemonTypes.PSYCHIC)


async def directing_traffic(ctx):
    """Look at the top 5 cards of your deck and put them back in any order."""
    await ctx.reorder_deck_top(5)


def _can_pay_attack(ctx, ability) -> bool:
    attacker = ctx.attacker
    if attacker is None:
        return False
    printed = getattr(ability, "cost", None) or {}
    cost = {CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(int(k))]: v
            for k, v in printed.items()}
    need = dict(effective_attack_cost(ctx.board, attacker, cost))
    return attack_cost_satisfied(
        need, ctx.board.attached_energies(attacker), ctx.board)


async def copy_anything(ctx):
    """Copy 1 of the opponent's in-play attacks; fizzle without the Energy."""
    candidates = []
    seen = set()
    for pokemon in ctx.opponent_pokemon_in_play():
        definition = def_for(pokemon.archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, Attack):
                continue
            key = (ability.title, ability.game_text)
            if key in seen:
                continue
            seen.add(key)
            candidates.append((pokemon, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not _can_pay_attack(ctx, chosen):
        return
    if getattr(chosen, "gx", False):
        if gx_used(ctx) or gx_attacks_blocked(ctx.board, ctx.player_id, ctx.attacker):
            return
        ctx.session.turn_state.gx_used.add(ctx.player_id)
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(
                    ctx.attacker.entity_id, entry["abilityID"])


# ======================================================================
# On-play
# ======================================================================

async def pantomime(ctx):
    """You may switch 1 of your face-down Prizes with the top card of your deck."""
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    if not prize_area or not prize_area.children or not deck or not deck.children:
        return
    if not await ctx.ask_yes_no(
            "Switch 1 of your face-down Prize cards with the top card of your deck?"):
        return
    session = ctx.session
    await ctx.flush_choreography()
    prize_ids = [c.entity_id for c in prize_area.children]
    picked = await session._prompt_prize_pick(
        ctx.player_id, prize_ids, 1,
        prompt="Choose 1 of your Prize cards to switch with the top card of your deck.",
        prize_area=prize_area,
    )
    prize_card = ctx.board.get_entity(picked[0]) if picked else None
    if prize_card is None:
        return
    slot = prize_card.board_slot
    if slot is None:
        slot = list(prize_area.children).index(prize_card)
    top_card = deck.children[-1]
    moves = []
    if ctx.board.move_card(prize_card.entity_id, deck.entity_id):
        moves.append(session._entity_moved_msg(
            prize_card.entity_id, deck.entity_id, len(deck.children) - 1))
    if ctx.board.move_card(top_card.entity_id, prize_area.entity_id, slot):
        moves.append(session._entity_moved_msg(
            top_card.entity_id, prize_area.entity_id, slot))
    if moves:
        await session.send_game_sequence(
            list(session.players.values()),
            GameSequence.WITH_OPEN_PRIZE_CARDS, moves)
    ctx.visual_targets = [prize_area.entity_id, deck.entity_id]
