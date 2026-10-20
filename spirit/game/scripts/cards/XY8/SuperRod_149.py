from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_pokemon_card


def super_rod_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    if discard is None:
        return False
    pool = [
        c for c in discard.children
        if is_pokemon_card(c) or is_basic_energy_card(c)
    ]
    return len(pool) >= 3


async def super_rod(ctx):
    """Shuffle 3 in any combination of Pokémon and basic Energy into deck."""
    pool = [
        c for c in ctx.discard_pile()
        if is_pokemon_card(c) or is_basic_energy_card(c)
    ]
    if len(pool) < 3:
        return
    picks = await ctx.choose_cards(
        pool, 3, minimum=3,
        prompt="Choose 3 Pokémon and/or basic Energy cards to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


card = ItemCardDef(
    guid="dffbeedc-023d-5e43-ae2a-3db735d2e307",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod", "Item"],
    subtypes=["Item"],
    collector_number=149,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    condition=super_rod_condition,
    effect=super_rod,
)
