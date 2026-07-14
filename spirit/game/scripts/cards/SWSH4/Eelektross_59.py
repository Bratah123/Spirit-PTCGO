from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def electrified_bite_mark(ctx):
    """60 damage."""
    await ctx.deal_damage()


async def electrified_bite_mark_watch(ctx):
    """During opponent's next turn, if they attach an Energy card from
    hand to the Defending Pokémon, put 6 damage counters on it."""
    if not ctx.attack_used_last_turn(title="Electrified Bite Mark", entity=ctx.source):
        return
    if ctx.attaching_player_id != ctx.opponent_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None or receiver is not ctx.opponent_active():
        return
    await ctx.deal_damage(60, target=receiver, apply_modifiers=False, as_counters=True)


async def electro_sprinkler(ctx):
    await ctx.deal_damage()
    my_bench = ctx.my_bench()
    if my_bench:
        target = await ctx.choose_pokemon(
            my_bench, "Choose 1 of your Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(30, target=target, apply_modifiers=False)
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        target2 = await ctx.choose_pokemon(
            opp_bench, "Choose 1 of your opponent's Benched Pokémon")
        if target2 is not None:
            await ctx.deal_damage(30, target=target2, apply_modifiers=False)


card = PokemonCardDef(
    guid="685ebc6c-a630-52be-85f4-698bb2b2960b",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Eelektross"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Electrified Bite Mark",
            game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pokémon, put 6 damage counters on that Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=electrified_bite_mark,
        ),
        Ability(
            title="Electrified Bite Mark",
            game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pokémon, put 6 damage counters on that Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=electrified_bite_mark_watch,
        ),
        Attack(
            title="Electro Sprinkler",
            game_text="This attack also does 30 damage to 1 of your Benched Pokémon and 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=electro_sprinkler,
        ),
    ],
)
