from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities


async def boost_shake(ctx):
    """Search a card that evolves from 1 of your Pokemon, evolve it immediately, shuffle. Your turn ends."""
    candidates = ctx.my_pokemon_in_play()
    if candidates:
        target = await ctx.choose_pokemon(candidates, "Choose a Pokémon to evolve")
        logic_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) if target else None
        if logic_name:
            picks = await ctx.search_deck(
                lambda c, name=logic_name: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
                count=1, minimum=0,
                prompt="Choose a card that evolves from that Pokémon.",
            )
            if picks:
                await ctx.evolve_pokemon(target, picks[0])
        await ctx.shuffle_deck()
    ctx.ends_turn = True


card = ItemCardDef(
    guid="33b51511-fbd6-572b-8df8-11df705cbea4",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BoostShake.Name",
    display_name="Boost Shake",
    searchable_by=["Boost Shake", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=boost_shake,
)
