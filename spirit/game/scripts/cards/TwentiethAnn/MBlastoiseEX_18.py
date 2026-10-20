from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _dread_launcher(ctx):
    """180; flip a coin. If tails, discard 2 Water Energy attached to this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]):
        n = min(2, sum(1 for e in ctx.attached_energies(ctx.attacker) if _is_water_energy(e)))
        if n:
            await ctx.discard_energy_from(ctx.attacker, n, predicate=_is_water_energy, minimum=n)


card = PokemonCardDef(
    guid="6b301604-89ed-5385-971c-9bc18bbb8eff",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBlastoiseEX.Name",
    display_name="M Blastoise-EX",
    searchable_by=["M Blastoise-EX", "MEGA", "EX", "MBlastoiseEX"],
    subtypes=["MEGA", "EX"],
    collector_number=18,
    set_code="TwentiethAnn",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    family_id=9,
    abilities=[
        Attack(
            title="Dread Launcher",
            game_text="Flip a coin. If tails, discard 2 Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=_dread_launcher,
        ),
    ],
)