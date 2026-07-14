from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def _moomoo_condition(board, player_id):
    return any(board.attached_energies(p) for p in board.pokemon_in_play(player_id))


async def moomoo_cheese(ctx):
    """Heal 30 damage from up to 2 of your Pokemon that have Energy attached."""
    candidates = [p for p in ctx.my_pokemon_in_play() if ctx.attached_energies(p)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 2, minimum=0,
        prompt="Choose up to 2 Pokémon with Energy attached to heal",
    )
    for pokemon in picks:
        await ctx.heal(30, pokemon)


card = ItemCardDef(
    guid="4e064c92-770c-58fb-905d-647375971e8b",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoomooCheese.Name",
    display_name="Moomoo Cheese",
    searchable_by=["Moomoo Cheese", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    effect=moomoo_cheese,
    condition=_moomoo_condition,
)
