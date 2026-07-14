from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_damaged_pokemon


async def sweet_honey(ctx):
    """Choose 1 of your Pokemon, flip a coin until tails, heal 40 per heads."""
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon."
    )
    if target is None:
        return
    heads = await ctx.flip_until_tails("Sweet Honey")
    if heads:
        await ctx.heal(40 * heads, target=target)


card = ItemCardDef(
    guid="d4fd0d96-df66-5e9d-ad5d-3cae2843aeaa",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SweetHoney.Name",
    display_name="Sweet Honey",
    searchable_by=["Sweet Honey", "Item"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=sweet_honey,
    condition=requires_damaged_pokemon(),
)
