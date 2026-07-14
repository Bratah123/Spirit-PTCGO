from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


async def power_whip(ctx):
    """20 damage to 1 of your opponent's Pokemon for each Energy attached
    to this Pokemon. (No W/R for Benched targets.)"""
    amount = 20 * count_energy("self")(ctx)
    if amount <= 0:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon to take damage.")
    if target is not None:
        await ctx.deal_damage(amount, target=target)


async def time_out_kick(ctx):
    """100 damage. You may put an Energy attached to the opponent's Active
    into their hand."""
    await ctx.deal_damage()
    defender = ctx.opponent_active()
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Put an Energy attached to your opponent's Active Pokémon into their hand?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy card to put into your opponent's hand.")
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="beb9e421-3375-5639-a705-b726c3f73565",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name",
    display_name="Tsareena",
    searchable_by=["Tsareena", "Stage 2", "Tsareena"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="SWSH3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Power Whip",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=power_whip,
        ),
        Attack(
            title="Time Out Kick",
            game_text="You may put an Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=time_out_kick,
        ),
    ],
)