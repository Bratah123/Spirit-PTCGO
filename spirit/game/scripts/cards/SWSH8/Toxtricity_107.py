from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def punk_shock(ctx):
    """70 damage. You may Paralyze the opponent's Active; if you do, this Pokemon also does 70 to itself."""
    await ctx.deal_damage()
    if await ctx.ask_yes_no(
        "Make your opponent's Active Pokémon Paralyzed? If you do, this "
        "Pokémon also does 70 damage to itself."
    ):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        await ctx.deal_damage(70, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="1b65c547-a2a7-5e43-b743-681c0bb39b81",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SWSH8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Punk Shock",
            game_text="You may choose to make your opponent's Active Pok\u00e9mon Paralyzed. If you do, this Pok\u00e9mon also does 70 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=punk_shock,
        ),
    ],
)