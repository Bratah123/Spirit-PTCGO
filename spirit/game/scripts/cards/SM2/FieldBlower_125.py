from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import _tools_and_stadium


def field_blower_playable(board, player_id):
    return bool(_tools_and_stadium(board))


async def field_blower(ctx):
    """Discard up to 2 in any combination of Tools and Stadiums in play."""
    targets = _tools_and_stadium(ctx.board)
    if not targets:
        return
    picks = await ctx.choose_cards(
        targets, min(2, len(targets)), minimum=0,
        prompt="Choose up to 2 Pokémon Tool and/or Stadium cards to discard.",
    )
    if picks:
        await ctx.discard_cards(picks)


card = ItemCardDef(
    guid="082b68b0-2d81-5a61-b768-9ede95750cbf",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieldBlower.Name",
    display_name="Field Blower",
    searchable_by=["Field Blower", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=field_blower_playable,
    effect=field_blower,
)
