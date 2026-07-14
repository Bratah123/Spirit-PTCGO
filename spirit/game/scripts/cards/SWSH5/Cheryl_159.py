from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.effects import is_evolution_pokemon


async def cheryl(ctx):
    """Heal all damage from each Evolution Pokemon; discard all Energy from
    the ones healed this way."""
    for pokemon in ctx.my_pokemon_in_play():
        if not is_evolution_pokemon(pokemon):
            continue
        if pokemon.get_attribute(AttrID.HP, 0) >= ctx.max_hp(pokemon):
            continue
        healed = await ctx.heal(ctx.max_hp(pokemon), target=pokemon)
        if healed:
            energies = ctx.attached_energies(pokemon)
            if energies:
                await ctx.discard_cards(energies)


card = SupporterCardDef(
    guid="5b62307a-a7da-5e4b-8bcf-6f4082d95e29",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cheryl.Name",
    display_name="Cheryl",
    searchable_by=["Cheryl", "Supporter"],
    subtypes=["Supporter"],
    collector_number=159,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    effect=cheryl,
)
