from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def hurricane_shock(ctx):
    """Flip 4 coins. 50 damage for each heads; if at least 2 are heads, the
    opponent's Active Pokémon is now Paralyzed."""
    results = await ctx.flip_coins(4, "Hurricane Shock")
    heads = sum(1 for r in results if r)
    if heads > 0:
        await ctx.deal_damage(heads * 50)
    if heads >= 2:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="6299830c-db10-5d94-b580-5c13937f4793",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Hurricane Shock",
            game_text="Flip 4 coins. This attack does 50 damage for each heads. If at least 2 of them are heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="x",
            effect=hurricane_shock,
        ),
    ],
)