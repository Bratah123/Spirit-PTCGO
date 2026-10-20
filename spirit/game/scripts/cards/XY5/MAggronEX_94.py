from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _megaton_slam(ctx):
    """120; you may flip: heads +120, tails 20 to each of your Benched Pokemon."""
    if not await ctx.ask_yes_no("Flip a coin for Megaton Slam?"):
        await ctx.deal_damage()
        return
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        await ctx.deal_damage(240)
        return
    await ctx.deal_damage()
    for p in ctx.my_bench():
        await ctx.deal_damage(20, target=p)


card = PokemonCardDef(
    guid="0dd7b90b-267b-5998-889c-835209515be0",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAggronEX.Name",
    display_name="M Aggron-EX",
    searchable_by=["M Aggron-EX", "MEGA", "EX", "MAggronEX"],
    subtypes=["MEGA", "EX"],
    collector_number=94,
    set_code="XY5",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AggronEX.Name",
    family_id=306,
    abilities=[
        Attack(
            title="Megaton Slam",
            game_text="You may flip a coin. If heads, this attack does 120 more damage. If tails, this attack does 20 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=_megaton_slam,
        ),
    ],
)