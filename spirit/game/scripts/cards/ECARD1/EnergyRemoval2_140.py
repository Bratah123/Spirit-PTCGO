from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_energy_attached


async def energy_removal_2(ctx):
    """Flip a coin. If heads, discard 1 Energy from 1 of opponent's Pokémon."""
    results = await ctx.flip_coins(1, "Energy Removal 2")
    if not results or not results[0]:
        return
    candidates = [p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.discard_energy_from(target, 1)


card = ItemCardDef(
    guid="d1e0df22-cbc3-593d-a852-55e0b47f0abf",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2"],
    subtypes=[],
    collector_number=140,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=energy_removal_2,
    condition=opponent_has_energy_attached,
)
