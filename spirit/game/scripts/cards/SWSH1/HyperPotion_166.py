from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.models.board import BoardState
from spirit.game.session.legal_actions import energy_provided_count


def _has_two_energy(board, pokemon):
    return sum(
        energy_provided_count(energy, board)
        for energy in BoardState.attached_energies(pokemon)
    ) >= 2


def _hyper_potion_playable(board, player_id):
    return any(
        _has_two_energy(board, pokemon)
        for pokemon in board.pokemon_in_play(player_id)
    )


async def hyper_potion(ctx):
    """Heal 120 from 1 of your Pokemon with >=2 Energy attached; if healed, discard 2 Energy from it."""
    candidates = [
        pokemon for pokemon in ctx.my_pokemon_in_play()
        if _has_two_energy(ctx.board, pokemon)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with at least 2 Energy attached"
    )
    if target is None:
        return
    healed = await ctx.heal(120, target)
    if healed:
        await ctx.discard_energy_units_from(
            target, 2, prompt="Discard 2 Energy"
        )


card = ItemCardDef(
    guid="a50f6b61-4dbe-572f-820e-64500bb93bf9",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperPotion.Name",
    display_name="Hyper Potion",
    searchable_by=["Hyper Potion", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=hyper_potion,
    condition=_hyper_potion_playable,
)
