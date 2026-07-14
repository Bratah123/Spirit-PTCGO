from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card


async def candela(ctx):
    """Draw 2. If you drew any cards, flip a coin; heads attaches a Fire
    Energy card from your discard pile to 1 of your Benched Pokemon."""
    drawn = await ctx.draw_cards(2)
    if drawn <= 0:
        return
    heads = (await ctx.flip_coins(1, "Candela"))[0]
    if not heads:
        return
    bench = ctx.my_bench()
    energies = [
        c for c in ctx.discard_pile()
        if is_basic_energy_card(c)
        and PokemonTypes.FIRE.value in (c.get_attribute(AttrID.POKEMON_TYPES) or [])
    ]
    if not bench or not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Fire Energy card from your discard pile.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach Fire Energy to"
    )
    if target is not None:
        await ctx.attach_energy(picks[0], target)


card = SupporterCardDef(
    guid="71160c61-af09-5d56-aafd-b1886d76a0d4",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Candela.Name",
    display_name="Candela",
    searchable_by=["Candela", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="PGO",
    rarity=Rarities.RareRainbow,
    effect=candela
)
