from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.ancient_traits import ancient_trait
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
    guid="515531db-3a2d-5b98-9067-b53e6b6737a5",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        ancient_trait('θ Double'),
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