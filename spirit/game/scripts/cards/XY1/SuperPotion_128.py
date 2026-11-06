from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon, _is_damaged


async def super_potion(ctx):
    """Heal 60 damage from 1 of your Pok\u00e9mon. If you do, discard an Energy
    attached to that Pok\u00e9mon."""
    damaged = [p for p in ctx.my_pokemon_in_play() if _is_damaged(ctx.board, p)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose 1 of your Pok\u00e9mon to heal") or damaged[0]
    healed = await ctx.heal(60, target)
    if healed and ctx.attached_energies(target):
        await ctx.discard_energy_from(target, 1, minimum=1, prompt="Choose an Energy to discard")


card = ItemCardDef(
    guid="ba4e49c8-3fab-584e-b664-207889afcbbe",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=super_potion,
    condition=requires_damaged_pokemon(),
)
