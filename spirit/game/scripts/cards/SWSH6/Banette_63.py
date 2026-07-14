from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def resolute_spite(ctx):
    """Put up to 7 damage counters on this Pokemon; 20 damage per counter placed."""
    n = await ctx.choose(
        "Put up to 7 damage counters on this Pokémon.",
        [str(i) for i in range(8)],
    )
    if n > 0:
        await ctx.deal_damage(n * 10, target=ctx.attacker, as_counters=True)
        await ctx.deal_damage(20 * n)


card = PokemonCardDef(
    guid="d2706007-e561-56fb-86e2-0ddc9c9b81dc",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Single Strike", "Banette"],
    subtypes=["Stage 1", "Single Strike"],
    collector_number=63,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Resolute Spite",
            game_text="Put up to 7 damage counters on this Pokémon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=resolute_spite,
        ),
        Attack(
            title="Eerie Light",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
