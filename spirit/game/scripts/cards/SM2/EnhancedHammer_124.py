from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_special_energy
from spirit.game.session.effects import is_special_energy


def _opponent_with_special_energy(ctx):
    return [p for p in ctx.opponent_pokemon_in_play()
            if any(is_special_energy(e) for e in ctx.attached_energies(p))]


async def enhanced_hammer(ctx):
    """Discard a Special Energy from 1 of your opponent's Pokémon."""
    candidates = _opponent_with_special_energy(ctx)
    if not candidates:
        return
    target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.discard_energy_from(
        target, 1, predicate=is_special_energy,
        prompt="Choose a Special Energy to discard.",
    )


card = ItemCardDef(
    guid="074bf196-9dd8-535f-9e27-1db505665b8d",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=opponent_has_special_energy,
    effect=enhanced_hammer,
)
