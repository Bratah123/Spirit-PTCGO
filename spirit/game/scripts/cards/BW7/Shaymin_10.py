from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


async def _leaf_drain(ctx):
    """Printed damage. Flip a coin; if heads, heal 30 damage from this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Leaf Drain")
    if results and results[0]:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="79386055-e551-5742-b1ef-ff18a1b0dd66",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for 2 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Leaf Drain",
            game_text="Flip a coin. If heads, heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=_leaf_drain,
        ),
    ],
)