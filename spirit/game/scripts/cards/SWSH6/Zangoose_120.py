from spirit.game.data_utils import PokemonCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, TrainerType


def _rapid_strike_supporter_played(ctx):
    return ctx.played_trainer_this_turn(
        lambda r: r[2] == TrainerType.SUPPORTER.value
        and "Rapid Strike" in subtypes_for(r[0])
    ) > 0


async def gale_claws(ctx):
    """50, plus 50 to 2 opposing Benched if a Rapid Strike Supporter was played this turn."""
    await ctx.deal_damage()
    if not _rapid_strike_supporter_played(ctx):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    targets = await ctx.choose_cards(
        bench, 2, prompt="Choose 2 of your opponent's Benched Pokémon"
    )
    for target in targets:
        await ctx.deal_damage(50, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="78dad1b0-ff63-585a-98c9-3ff0b6ad0719",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic", "Rapid Strike", "Zangoose"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=120,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Gale Claws",
            game_text="If you played a Rapid Strike Supporter card from your hand during this turn, this attack also does 50 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=gale_claws,
        ),
    ],
)