from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def hazard_star(ctx):
    if await ctx.ask_yes_no(
        "Make your opponent's Active Pokémon Paralyzed and Poisoned?"
    ):
        defender = ctx.opponent_active()
        if defender is not None:
            await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
            await ctx.apply_special_condition(
                defender, SpecialConditions.POISONED, poison_counters=3
            )


async def big_bang_arm(ctx):
    counters = (ctx.max_hp(ctx.attacker) - ctx.attacker.get_attribute(AttrID.HP, 0)) // 10
    await ctx.deal_damage(max(0, 250 - 10 * counters))


card = PokemonCardDef(
    guid="074ceea7-aae2-59b9-ab1c-3de4efe41100",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionVSTAR.Name",
    display_name="Drapion VSTAR",
    searchable_by=["Drapion VSTAR", "VSTAR", "DrapionVSTAR"],
    subtypes=["VSTAR"],
    collector_number=200,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionV.Name",
    family_id=452,
    abilities=[
        Ability(
            title="Hazard Star",
            game_text="During your turn, you may make your opponent's Active Pok\u00e9mon Paralyzed and Poisoned. During Pok\u00e9mon Checkup, put 3 damage counters on that Pok\u00e9mon instead of 1. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=hazard_star,
        ),
        Attack(
            title="Big Bang Arm",
            game_text="This attack does 10 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=250,
            damage_operator="-",
            effect=big_bang_arm,
        ),
    ],
)