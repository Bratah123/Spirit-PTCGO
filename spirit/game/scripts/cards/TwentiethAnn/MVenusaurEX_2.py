from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage


async def _bloom_buster(ctx):
    """130; flip a coin. If heads, 30 damage to each of the opponent's Benched Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        await spread_damage(30)(ctx)


card = PokemonCardDef(
    guid="dcd25acc-73d0-5144-ac99-87f0f606f51d",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MVenusaurEX.Name",
    display_name="M Venusaur-EX",
    searchable_by=["M Venusaur-EX", "MEGA", "EX", "MVenusaurEX"],
    subtypes=["MEGA", "EX"],
    collector_number=2,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.VenusaurEX.Name",
    family_id=3,
    abilities=[
        Attack(
            title="Bloom Buster",
            game_text="Flip a coin. If heads, this attack does 30 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=_bloom_buster,
        ),
    ],
)