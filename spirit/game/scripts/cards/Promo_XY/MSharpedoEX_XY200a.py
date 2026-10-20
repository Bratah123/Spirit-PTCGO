from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _torpedo_dive(ctx):
    """120; 10 to each opposing Benched Pokemon per [C] in its Retreat Cost."""
    await ctx.deal_damage()
    for p in ctx.opponent_bench():
        cost = p.get_attribute(AttrID.RETREAT_COST) or 0
        if isinstance(cost, dict):
            cost = sum(cost.values())
        if cost:
            await ctx.deal_damage(10 * int(cost), target=p, apply_modifiers=False)


card = PokemonCardDef(
    guid="6c71bd12-b5b3-5dfc-96f6-0147d2f51643",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSharpedoEX.Name",
    display_name="M Sharpedo-EX",
    searchable_by=["M Sharpedo-EX", "MEGA", "EX", "MSharpedoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=216,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name",
    family_id=319,
    abilities=[
        Attack(
            title="Torpedo Dive",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon for each Colorless in that Pok\u00e9mon's Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_torpedo_dive,
        ),
    ],
)