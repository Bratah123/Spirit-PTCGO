from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_random_from_hand


async def silent_shot(ctx):
    """Discard a random card from your opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, player_id=ctx.opponent_id, count=1)


async def hydro_snipe(ctx):
    """You may put an Energy attached to your opponent's Active Pokémon into their hand."""
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
        energies, 1, prompt="Choose an Energy to put into your opponent's hand",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="69f74ec2-8a1d-59ad-84fd-a9ab666a182e",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Inteleon"],
    subtypes=["Stage 2"],
    collector_number=59,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Silent Shot",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=silent_shot,
        ),
        Attack(
            title="Hydro Snipe",
            game_text="You may put an Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=hydro_snipe,
        ),
    ],
)