from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def burning_licks(ctx):
    """70 damage; flip 2 coins, discard an Energy from the opponent's Active per heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(2, "Burning Licks")
    count = sum(heads)
    if count and not ctx.effects_blocked(ctx.defender):
        await ctx.discard_energy_from(ctx.defender, count)


card = PokemonCardDef(
    guid="a0aa636d-2169-5583-ae55-35c24e9d6281",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Burning Licks",
            game_text="Flip 2 coins. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=burning_licks,
        ),
    ],
)