from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _nyan_press(ctx):
    """40+; heads 40 more; tails the opponent's Active is Paralyzed."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    heads = bool(results and results[0])
    await ctx.deal_damage(ctx.ability.damage + (40 if heads else 0))
    if not heads:
        await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="c87741d2-941e-5310-a988-100bc8c475ba",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purugly.Name",
    display_name="Purugly",
    searchable_by=["Purugly", "Stage 1", "Purugly"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glameow.Name",
    family_id=431,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Nyan Press",
            game_text="Flip a coin. If heads, this attack does 40 more damage. If tails, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=_nyan_press,
        ),
    ],
)