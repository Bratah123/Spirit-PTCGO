from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


async def power_rush(ctx):
    """120 damage. Flip a coin. If tails, this Pokémon can't attack during your next turn."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Power Rush"))[0]
    if not heads:
        lock_all_attacks(ctx, ctx.attacker)


def _is_darkness_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.DARKNESS.value)


async def _oblivion_wing(ctx):
    """30; attach a Darkness Energy card from your discard pile to 1 of your
    Benched Pokemon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    cards = [c for c in ctx.discard_pile() if _is_darkness_energy_card(c)]
    if not bench or not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Darkness Energy card")
    if not picks:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to attach it to")
    await ctx.attach_energy(picks[0], target or bench[0])


card = PokemonCardDef(
    guid="7bbeb23e-79cf-58dd-bbfd-37d9bdd4d87b",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title="Oblivion Wing",
            game_text="Attach a Darkness Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=_oblivion_wing,
        ),
        Attack(
            title="Darkness Blade",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=power_rush,
        ),
    ],
)