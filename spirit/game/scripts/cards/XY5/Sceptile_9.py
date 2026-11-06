from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import flip_bonus


async def _power_poison(ctx):
    """120; discard 1 Energy from this Pokemon; the opponent's Active is Poisoned."""
    await ctx.deal_damage()
    if ctx.attached_energies(ctx.attacker):
        await ctx.discard_energy_from(ctx.attacker, 1, minimum=1, prompt="Discard an Energy")
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="6ed35fc5-7131-5f97-ac68-91569ecd533b",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptile.Name",
    display_name="Sceptile",
    searchable_by=["Sceptile", "Stage 2", "Sceptile"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=252,
    abilities=[
        ancient_trait('Ω Barrier'),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Power Poison",
            game_text="Discard 1 Energy attached to this Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_power_poison,
        ),
    ],
)