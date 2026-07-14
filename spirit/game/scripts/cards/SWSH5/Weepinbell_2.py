from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def dangerous_mucus(ctx):
    """On evolve: you may make opponent's Active Burned and Poisoned."""
    if await ctx.ask_yes_no("Make your opponent's Active Pokémon Burned and Poisoned?"):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="799ddb96-0b03-5a3d-a7e5-6c7cbe9b5905",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    display_name="Weepinbell",
    searchable_by=["Weepinbell", "Stage 1", "Weepinbell"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Dangerous Mucus",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may make your opponent's Active Pok\u00e9mon Burned and Poisoned.",
            trigger=Triggers.ON_EVOLVE,
            effect=dangerous_mucus,
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)