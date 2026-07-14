from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_in_play
from spirit.game.models.board import BoardState


def _has_two_energy(pokemon):
    return len(BoardState.attached_energies(pokemon)) >= 2


async def hyper_potion(ctx):
    """Heal 120 from 1 of your Pokemon with >=2 Energy attached; if healed, discard 2 Energy from it."""
    candidates = [p for p in ctx.my_pokemon_in_play() if _has_two_energy(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with at least 2 Energy attached"
    )
    if target is None:
        return
    healed = await ctx.heal(120, target)
    if healed:
        await ctx.discard_energy_from(target, 2, prompt="Discard 2 Energy")


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
    condition=requires_in_play(_has_two_energy),
)
