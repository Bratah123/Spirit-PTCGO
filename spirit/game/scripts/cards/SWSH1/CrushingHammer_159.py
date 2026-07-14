from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_energy_attached


async def crushing_hammer(ctx):
    """Flip a coin. If heads, discard an Energy from 1 of your opponent's Pokémon."""
    results = await ctx.flip_coins(1, "Crushing Hammer")
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
    guid="0f0d405a-bc01-5a5b-a5b6-7dec00073533",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=crushing_hammer,
    condition=opponent_has_energy_attached
)
