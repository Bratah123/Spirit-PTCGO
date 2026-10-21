from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def _slippery_soles(ctx):
    """Switch your Active with a Benched Pokémon; then your opponent switches
    their Active with 1 of their Benched Pokémon."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        opp_target = await ctx.choose_pokemon(
            opp_bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id)
        if opp_target is not None:
            await ctx.switch_active(ctx.opponent_id, opp_target)


def _slippery_soles_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


def _is_metal_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.METAL.value)


async def _iron_cannon(ctx):
    """80+; you may discard all Metal Energy on this Pokemon for 80 more."""
    metal = [e for e in ctx.attached_energies(ctx.attacker) if _is_metal_energy(e)]
    if metal and await ctx.ask_yes_no("Discard all Metal Energy for 80 more damage?"):
        await ctx.discard_cards(metal)
        await ctx.deal_damage(ctx.ability.damage + 80)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="ba0642e5-af29-5fb2-b815-7fd2d18df58f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=49,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Magnetic Warp",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_slippery_soles_condition,
            effect=_slippery_soles,
        ),
        Attack(
            title="Iron Cannon",
            game_text="You may discard all Metal Energy attached to this Pok\u00e9mon. If you do, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=_iron_cannon,
        ),
    ],
)