from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _burst_curse(ctx):
    """Discard 2 Energy attached to this Pokemon; put 8 damage counters on your
    opponent's Pokemon in any way you like."""
    n = min(2, len(ctx.attached_energies(ctx.attacker)))
    if n:
        await ctx.discard_energy_from(ctx.attacker, n, minimum=n)
    await ctx.place_damage_counters(8)


card = PokemonCardDef(
    guid="69de54df-c55c-528e-b885-ba6e0f2a6cdf",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Burst Curse",
            game_text="Discard 2 Energy attached to this Pok\u00e9mon. Put 8 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=_burst_curse,
        ),
    ],
)