from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


async def pokedex(ctx):
    """Look at the top 5 cards of your deck and put them back on top in any order."""
    await ctx.reorder_deck_top(5)


card = ItemCardDef(
    guid="6a490558-dc70-5aa3-80ea-a2f3747a9725",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name",
    display_name="Pokédex",
    searchable_by=["Pokédex", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=pokedex,
)
