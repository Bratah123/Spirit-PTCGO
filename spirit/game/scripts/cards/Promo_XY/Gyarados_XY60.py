from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.content.definitions import def_for


async def _full_retaliation(ctx):
    """30+; 30 more for each damage counter on each of your Benched Magikarp."""
    n = sum((ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10 for p in ctx.my_bench()
            if getattr(def_for(p.archetype_id), "display_name", None) == "Magikarp")
    await ctx.deal_damage(ctx.ability.damage + 30 * max(0, n))


async def _thrash(ctx):
    """100+; heads +30, tails 30 damage to this Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        await ctx.deal_damage(ctx.ability.damage + 30)
    else:
        await ctx.deal_damage()
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="14c436c2-3657-5cb6-88d5-b7e1b9479496",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Full Retaliation",
            game_text="This attack does 30 more damage for each damage counter on each of your Benched Magikarp.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=_full_retaliation,
        ),
        Attack(
            title="Thrash",
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=_thrash,
        ),
    ],
)