from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage


async def _sludge_crash(ctx):
    """Printed damage; flip until tails, discard an Energy from the Defending
    Pokemon for each heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    d = ctx.defender
    if heads and d is not None and not ctx.effects_blocked(d):
        n = min(heads, len(ctx.attached_energies(d)))
        if n:
            await ctx.discard_energy_from(d, n, minimum=n)


card = PokemonCardDef(
    guid="0f677241-a15c-5aca-96aa-6e29db97f604",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2", "Feraligatr"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Hyper Whirlpool",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_sludge_crash,
        ),
        Attack(
            title="Second Strike",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(has_damage(), 80),
        ),
    ],
)