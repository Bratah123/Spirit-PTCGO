from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def superpower(ctx):
    """You may do 20 more damage; if you do, this Pokémon does 20 to itself."""
    if await ctx.ask_yes_no(
        "Do 20 more damage? If you do, this Pokémon does 20 damage to itself."
    ):
        await ctx.deal_damage(80)
        await ctx.deal_damage(20, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage(60)


async def _tender_vengeance(ctx):
    """Flip a coin; heads: 10 times the damage counters on your Benched Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]):
        return
    n = sum(damage_counters_on(lambda c, p=p: p)(ctx) for p in ctx.my_bench())
    await ctx.deal_damage(10 * n)


card = PokemonCardDef(
    guid="eadae8e0-d1be-5653-9877-91c7f7810a7f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Attack(
            title="Tender Vengeance",
            game_text="Flip a coin. If heads, this attack does 10 damage times the number of damage counters on each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="x",
            effect=_tender_vengeance,
        ),
        Attack(
            title="Charge Dash",
            game_text="You may do 20 more damage. If you do, this Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=superpower,
        ),
    ],
)