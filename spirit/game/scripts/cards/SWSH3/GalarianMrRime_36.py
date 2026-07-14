from spirit.game.card_effects.attacks_common import damage_per, count_discard, has_attack_titled
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, GameSequence


def _shuffle_dance_condition(board, player_id, pokemon):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    if opponent is None:
        return False
    prizes = board.find_player_area(opponent, "prizePile")
    deck = board.find_player_area(opponent, "deck")
    return bool(prizes and prizes.children and deck and deck.children)


async def shuffle_dance(ctx):
    """Switch 1 of the opponent's face-down Prizes with the top card of their
    deck; both cards stay face down (no intros to either viewer)."""
    session = ctx.session
    prize_area = ctx.board.find_player_area(ctx.opponent_id, "prizePile")
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    if not prize_area or not prize_area.children or not deck or not deck.children:
        return
    await ctx.flush_choreography()
    prize_ids = [c.entity_id for c in prize_area.children]
    picked = await session._prompt_prize_pick(
        ctx.player_id, prize_ids, 1,
        prompt="Choose 1 of your opponent's Prize cards to switch with the top card of their deck.",
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
        # WithOpenPrizeCards tears the pick fan down (d.t cancels the explore
        # command); the slot is refilled in the same bracket so gaps are unchanged.
        await session.send_game_sequence(
            list(session.players.values()),
            GameSequence.WITH_OPEN_PRIZE_CARDS, moves)
    ctx.visual_targets = [prize_area.entity_id, deck.entity_id]


card = PokemonCardDef(
    guid="f6bc1751-21f2-5e0e-bf61-04c023ebab4d",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrRime.Name",
    display_name="Galarian Mr. Rime",
    searchable_by=["Galarian Mr. Rime", "Stage 1", "GalarianMrRime"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    family_id=122,
    abilities=[
        Ability(
            title="Shuffle Dance",
            game_text="Once during your turn, you may switch 1 of your opponent's face-down Prize cards with the top card of their deck. (The cards stay face down.)",
            activation=Activations.ONCE_PER_TURN,
            condition=_shuffle_dance_condition,
            effect=shuffle_dance,
        ),
        Attack(
            title="Mad Party",
            game_text="This attack does 20 damage for each Pok\u00e9mon in your discard pile that has the Mad Party attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_discard("mine", has_attack_titled("Mad Party")), 20),
        ),
    ],
)