from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


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
    guid="4348003f-bad0-5d75-ba0e-0c00b844421f",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name",
    display_name="Roserade",
    searchable_by=["Roserade", "Stage 1", "Roserade"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    family_id=315,
    abilities=[
        Attack(
            title="Whiplash",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_sludge_crash,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3},
            damage=70,
            effect=heal_attack(20),
        ),
    ],
)