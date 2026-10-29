from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def max_potion(ctx):
    """Heal all damage from 1 of your Pokémon. If you do, discard all Energy
    from that Pokémon."""
    damaged = [p for p in ctx.my_pokemon_in_play()
               if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
    if not damaged:
        return
    target = damaged[0] if len(damaged) == 1 else await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to heal")
    if target is None:
        return
    amount = ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)
    if amount <= 0:
        return
    await ctx.heal(amount, target)
    await ctx.discard_energy_from(target, 99)


card = ItemCardDef(
    guid="b2dcfc2b-bf83-51aa-8674-1b9090ea73f2",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=requires_damaged_pokemon(),
    effect=max_potion,
)
