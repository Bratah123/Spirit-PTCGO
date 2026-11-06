from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def fiery_torch_condition(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_fire_energy_card(c) for c in hand.children)


async def fiery_torch(ctx):
    """Discard a Fire Energy card from your hand, then draw 2 cards."""
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=_is_fire_energy_card,
                                         prompt="Discard a Fire Energy card")
    if picked:
        await ctx.draw_cards(2)


card = ItemCardDef(
    guid="681e3241-8931-5029-ad89-4f87f4eac748",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryTorch.Name",
    display_name="Fiery Torch",
    searchable_by=["Fiery Torch", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    effect=fiery_torch,
    condition=fiery_torch_condition
)
