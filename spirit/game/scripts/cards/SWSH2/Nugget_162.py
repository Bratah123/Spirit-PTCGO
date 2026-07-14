from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def _turn_drawn(board, player_id, card):
    """Playable only if drawn as this turn's draw AND before any other main
    action ("before you put it into your hand" -- immediate play; landing in
    hand first is the engine's accepted approximation)."""
    state = getattr(board, "turn_state", None)
    if state is None or card.entity_id not in state.turn_draw_entity_ids:
        return False
    return (
        not state.supporter_played and not state.energy_attached
        and not state.retreated and not state.trainers_played
        and not state.attacks_used and not state.used_abilities
        and state.turn_number not in state.entered_play_turn.values()
    )


async def _nugget(ctx):
    """Draw 3 cards."""
    await ctx.draw_cards(3)


card = ItemCardDef(
    guid="6479deb7-99e6-551e-a271-8bef6b9a7802",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nugget.Name",
    display_name="Nugget",
    searchable_by=["Nugget", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    condition=_turn_drawn,
    effect=_nugget,
)
