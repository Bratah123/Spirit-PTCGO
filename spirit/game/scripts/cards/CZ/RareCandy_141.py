from spirit.game.data_utils import ItemCardDef, evolves_from
from spirit.game.attributes import Rarities, AttrID, PokemonStage
from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card


def _stage2_matches(hand_cards, logic_name):
    return [
        c for c in hand_cards
        if is_pokemon_card(c)
        and c.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value
        and evolves_from(c.archetype_id, logic_name)
    ]


def _turn_eligible_basics(board, player_id):
    turn_state = getattr(board, "turn_state", None)
    if turn_state is None:
        return []
    return [
        p for p in board.pokemon_in_play(player_id)
        if is_basic_pokemon(p) and turn_state.may_evolve_target(p.entity_id)
    ]


def _rare_candy_condition(board, player_id):
    return bool(_turn_eligible_basics(board, player_id))


async def _rare_candy(ctx):
    """Choose a Basic Pokemon in play; if you have a Stage 2 in hand that evolves from it, put that card onto it, skipping the Stage 1."""
    candidates = _turn_eligible_basics(ctx.board, ctx.player_id)
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose a Basic Pokémon in play")
    if target is None:
        return
    logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    stage2_hand = _stage2_matches(ctx.hand(), logic_name) if logic_name else []
    if not stage2_hand:
        return
    picks = await ctx.choose_cards(
        stage2_hand, 1, prompt="Choose a Stage 2 Pokémon to evolve into",
    )
    if not picks:
        return
    await ctx.evolve_pokemon(target, picks[0])


card = ItemCardDef(
    guid="963902d0-48a5-507a-ae11-816234a0cd76",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RareCandy.Name",
    display_name="Rare Candy",
    searchable_by=["Rare Candy", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    effect=_rare_candy,
    condition=_rare_candy_condition,
)
