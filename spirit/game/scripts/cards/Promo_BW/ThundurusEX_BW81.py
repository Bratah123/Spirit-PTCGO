from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_team_plasma_pokemon, plasma_energy_attached
from spirit.game.card_effects.pokemon import is_energy_card


async def _raiden_knuckle(ctx):
    """Printed damage; attach an Energy card from your discard pile to 1 of
    your Benched Team Plasma Pokemon."""
    await ctx.deal_damage()
    bench = [p for p in ctx.my_bench() if is_team_plasma_pokemon(p)]
    pool = [c for c in ctx.discard_pile() if is_energy_card(c)]
    if not bench or not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy card to attach")
    if not picks:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Benched Team Plasma Pokémon")
    await ctx.attach_energy(picks[0], target or bench[0])


async def _thunderous_noise(ctx):
    """Printed damage; if this Pokemon has any Plasma Energy attached, discard
    an Energy attached to the Defending Pokemon."""
    await ctx.deal_damage()
    d = ctx.defender
    if (plasma_energy_attached(ctx.attacker) and d is not None
            and not ctx.effects_blocked(d) and ctx.attached_energies(d)):
        await ctx.discard_energy_from(d, 1, minimum=1)


card = PokemonCardDef(
    guid="da2c2d06-00fe-5ae8-a5e7-335f93c3d623",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusEX.Name",
    display_name="Thundurus-EX",
    searchable_by=["Thundurus-EX", "Basic", "EX", "Team Plasma", "ThundurusEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=81,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Attack(
            title="Raiden Knuckle",
            game_text="Attach an Energy card from your discard pile to 1 of your Benched Team Plasma Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=_raiden_knuckle,
        ),
        Attack(
            title="Thunderous Noise",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=_thunderous_noise,
        ),
    ],
)