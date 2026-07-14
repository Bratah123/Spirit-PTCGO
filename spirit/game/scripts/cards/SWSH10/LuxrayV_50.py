from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.effects import is_trainer_card


async def fang_snipe(ctx):
    """30 damage. Opponent reveals their hand; discard a Trainer card found there."""
    await ctx.deal_damage()
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    matches = [c for c in hand if is_trainer_card(c)]
    if not matches:
        return
    picks = await ctx.choose_cards(
        matches, 1, minimum=1,
        prompt="Choose a Trainer card to discard from your opponent's hand.",
        display_cards=hand,
    )
    await ctx.discard_cards(picks)


async def radiating_pulse(ctx):
    """Discard 2 Energy from this Pokémon. 120 damage. Opponent's Active is
    now Paralyzed."""
    await ctx.discard_energy_from(ctx.attacker, 2)
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="73ec0fc6-3960-54a0-82c5-f0a63808b832",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayV.Name",
    display_name="Luxray V",
    searchable_by=["Luxray V", "Basic", "V", "LuxrayV"],
    subtypes=["Basic", "V"],
    collector_number=50,
    set_code="SWSH10",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=405,
    abilities=[
        Attack(
            title="Fang Snipe",
            game_text="Your opponent reveals their hand. Discard a Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=fang_snipe,
        ),
        Attack(
            title="Radiating Pulse",
            game_text="Discard 2 Energy from this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=radiating_pulse,
        ),
    ],
)