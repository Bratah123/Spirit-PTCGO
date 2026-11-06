from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def pokemon_nurse(ctx):
    """Heal all damage from 1 of your Pokémon; discard all Energy from it."""
    damaged = [
        p for p in ctx.my_pokemon_in_play()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose 1 of your Pokémon")
    if target is None:
        return
    await ctx.heal(ctx.max_hp(target), target=target)
    energies = ctx.attached_energies(target)
    if energies:
        await ctx.discard_cards(energies)


card = SupporterCardDef(
    guid="14695a35-1796-5554-a762-fd808e6aa235",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonNurse.Name",
    display_name="Pokémon Nurse",
    searchable_by=["Pokémon Nurse", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=pokemon_nurse,
    condition=requires_damaged_pokemon(),
)
