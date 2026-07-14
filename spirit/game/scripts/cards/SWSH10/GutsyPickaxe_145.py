from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fighting_energy_card(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIGHTING.value)


async def gutsy_pickaxe(ctx):
    """Reveal the top card of your deck. If it's a Fighting Energy card,
    attach it to 1 of your Benched Pokemon; otherwise put it into your
    hand."""
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    await ctx.reveal_cards([card])
    if _is_fighting_energy_card(card):
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose a Benched Pokémon to attach the Energy to."
        )
        if target is not None:
            await ctx.attach_energy(card, target)
    else:
        await ctx.put_in_hand([card], reveal=False)


card = ItemCardDef(
    guid="f0cacb75-cb70-52c4-b02f-94d39e45d90b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GutsyPickaxe.Name",
    display_name="Gutsy Pickaxe",
    searchable_by=["Gutsy Pickaxe", "Item"],
    subtypes=["Item"],
    collector_number=145,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=gutsy_pickaxe
)
