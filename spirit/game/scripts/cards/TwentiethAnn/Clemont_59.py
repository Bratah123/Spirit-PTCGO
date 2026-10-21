from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _lightning(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value) \
        and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY)


async def clemont(ctx):
    """Search your deck for up to 4 Lightning Energy cards, reveal them, and put them into your hand; shuffle."""
    picks = await ctx.search_deck(_lightning, 4, minimum=0, prompt="Choose up to 4 Lightning Energy cards")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="4ea788ee-a424-53d9-99c6-b7709a2b0fa4",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clemont.Name",
    display_name="Clemont",
    searchable_by=["Clemont", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=clemont
)
