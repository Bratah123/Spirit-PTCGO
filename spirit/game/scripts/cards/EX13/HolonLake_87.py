"""EX13 Holon Phantoms — Holon Lake.
"""
from spirit.game.data_utils import StadiumCardDef, Attack
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.ex import holon_lake_passive, delta_draw_up_to


async def holon_lake_extra_draw(ctx):
    """If the Pokémon using this attack has δ, draw 2 cards."""
    a = ctx.attacker
    from spirit.game.card_effects.ex import _has_delta
    if a is not None and _has_delta(a):
        await ctx.draw_cards(2)


card = StadiumCardDef(
    guid="58b6e0bc-f74a-5f97-b04d-11c1b1473f99",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLake.Name",
    display_name="Holon Lake",
    searchable_by=["Holon Lake", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    passive=holon_lake_passive(),
    abilities=[
        Attack(
            title="Extra Draw",
            game_text="If the Pokémon using this attack has δ on its card, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=holon_lake_extra_draw,
        ),
    ],
)
