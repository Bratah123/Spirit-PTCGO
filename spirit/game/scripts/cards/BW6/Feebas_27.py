from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _add_a_dash(ctx):
    """Flip 2 coins. For each heads, draw a card."""
    results = await ctx.flip_coins(2, "Add-a-Dash")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.draw_cards(heads)


card = PokemonCardDef(
    guid="e8645082-32c9-5a44-94a5-14ca180db252",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Add-a-Dash",
            game_text="Flip 2 coins. For each heads, draw a card.",
            cost={PokemonTypes.WATER: 1},
            effect=_add_a_dash,
        ),
    ],
)