from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


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
    guid="121a4c13-9501-5e3b-83f3-77d9fdd57a83",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Spiteful Sigh",
            game_text="Put up to 7 damage counters on this Pok\u00e9mon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=resolute_spite,
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)