from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def eco_arm_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_is_tool(c) for c in discard.children)


async def eco_arm(ctx):
    """Shuffle 3 Pokemon Tool cards from your discard pile into your deck."""
    pool = [c for c in ctx.discard_pile() if _is_tool(c)]
    n = min(3, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 3 Pokémon Tool cards") if n else []
    if picks:
        await ctx.shuffle_into_deck(picks, ctx.player_id)


card = ItemCardDef(
    guid="81b11637-88ca-5d85-8101-26390a2fb766",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EcoArm.Name",
    display_name="Eco Arm",
    searchable_by=["Eco Arm", "Item"],
    subtypes=["Item"],
    collector_number=71,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=eco_arm,
    condition=eco_arm_condition
)
