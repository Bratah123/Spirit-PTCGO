from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.support_common import _is_damaged
from spirit.game.card_effects.pokemon import energy_provides_type


def _targets(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if _is_damaged(board, p)
            and any(energy_provides_type(e, PokemonTypes.FAIRY) for e in board.attached_energies(p))]


def fairy_drop_condition(board, player_id):
    return bool(_targets(board, player_id))


async def fairy_drop(ctx):
    """Heal 50 damage from 1 of your Pokemon that has any Fairy Energy attached to it."""
    target = await ctx.choose_pokemon(_targets(ctx.board, ctx.player_id), "Choose a Pok\u00e9mon to heal")
    if target is not None:
        await ctx.heal(50, target)


card = ItemCardDef(
    guid="1442d11a-2ff6-55a7-b23e-c7b37dc4fc0c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyDrop.Name",
    display_name="Fairy Drop",
    searchable_by=["Fairy Drop", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    condition=fairy_drop_condition,
    effect=fairy_drop
)
