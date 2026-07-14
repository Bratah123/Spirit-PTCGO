from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def wild_freeze(ctx):
    """70, plus 50 to itself; the opponent's Active is now Paralyzed."""
    await ctx.deal_damage()
    await ctx.deal_damage(50, target=ctx.attacker, apply_modifiers=False)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="ce4a0c8d-9f0f-5848-979a-46ff0a40d69e",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Attack(
            title="Ice Wing",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Wild Freeze",
            game_text="This Pokémon also does 50 damage to itself. Your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=70,
            effect=wild_freeze,
        ),
    ],
)
