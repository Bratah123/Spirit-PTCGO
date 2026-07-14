from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_energy_card
from spirit.game.card_effects.support_common import distribute_energy


def _is_fighting_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIGHTING.value in types


async def bea(ctx):
    """Discard the top 5 of your deck; attach any Energy discarded this way
    to your Benched Fighting Pokemon in any way you like."""
    cards = ctx.deck_top(5)
    await ctx.discard_cards(cards)
    energies = [c for c in cards if is_energy_card(c)]
    if not energies:
        return
    candidates = [p for p in ctx.my_bench() if _is_fighting_pokemon(p)]
    if not candidates:
        return
    await distribute_energy(ctx, energies, candidates)


card = SupporterCardDef(
    guid="e3f000c5-28b6-5581-b094-5c841b3cd836",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bea.Name",
    display_name="Bea",
    searchable_by=["Bea", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    effect=bea
)
