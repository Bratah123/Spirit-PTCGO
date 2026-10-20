from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _hyper_hypnosis(ctx):
    """When you attach an Energy from your hand to this Pokemon, you may make
    your opponent's Active Pokemon Asleep."""
    if (getattr(ctx, "attaching_player_id", None) != ctx.player_id
            or getattr(ctx, "energy_receiver", None) is not ctx.source):
        return
    target = ctx.opponent_active()
    if target is None or not await ctx.ask_yes_no("Use Hyper Hypnosis?"):
        return
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)


async def _maxamar(ctx):
    """Flip a coin for each Energy attached: 60 times the number of heads."""
    n = len(ctx.attached_energies(ctx.attacker))
    results = await ctx.flip_coins(n, ctx.ability.title) if n else []
    await ctx.deal_damage(60 * sum(1 for r in results or [] if r))


card = PokemonCardDef(
    guid="1f8682c8-7904-5dda-a588-e2c88e2f9be5",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MalamarEX.Name",
    display_name="Malamar-EX",
    searchable_by=["Malamar-EX", "Basic", "EX", "MalamarEX"],
    subtypes=["Basic", "EX"],
    collector_number=58,
    set_code="XY4",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=687,
    abilities=[
        Ability(
            title="Hyper Hypnosis",
            game_text="When you attach an Energy from your hand to this Pok\u00e9mon, you may use this Ability. Your opponent's Active Pok\u00e9mon is now Asleep.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_hyper_hypnosis,
        ),
        Attack(
            title="MAXamar",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=_maxamar,
        ),
    ],
)