from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.smp import shining_mane_passive


async def turbo_storm(ctx):
    """30 damage; attach 2 basic Energy from discard to 1 Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 2, minimum=0,
        prompt="Choose up to 2 basic Energy cards to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, target)


async def _grand_echo(ctx):
    """Heal all damage from all of your Pokemon."""
    for p in ctx.my_pokemon_in_play():
        await ctx.heal(ctx.max_hp(p), p)


card = PokemonCardDef(
    guid="a7921108-dc5d-545a-8d3b-d63b3adc1198",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name",
    display_name="Solgaleo-GX",
    searchable_by=["Solgaleo-GX", "Stage 2", "GX", "SolgaleoGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=104,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=791,
    abilities=[
        Ability(
            title="Shining Mane",
            game_text="Your Pok\u00e9mon in play have no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=shining_mane_passive,
        ),
        Attack(
            title="Turbo Strike",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=turbo_storm,
        ),
        Attack(
            title="Prominence-GX",
            game_text="Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_grand_echo,
        ),
    ],
)