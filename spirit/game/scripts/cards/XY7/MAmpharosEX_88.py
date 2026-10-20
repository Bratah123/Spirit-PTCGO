from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _exavolt(ctx):
    """120; you may do 50 more and Paralyze; if you do, 30 damage to this Pokemon."""
    if await ctx.ask_yes_no("Do 50 more damage and Paralyze (30 damage to this Pokémon)?"):
        await ctx.deal_damage(ctx.ability.damage + 50)
        await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)
        await ctx.deal_damage(30, target=ctx.attacker, apply_modifiers=False)
    else:
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="36f679aa-7878-50b0-ba8a-76ebc1947a98",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAmpharosEX.Name",
    display_name="M Ampharos-EX",
    searchable_by=["M Ampharos-EX", "MEGA", "EX", "MAmpharosEX"],
    subtypes=["MEGA", "EX"],
    collector_number=88,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosEX.Name",
    family_id=181,
    abilities=[
        Attack(
            title="Exavolt",
            game_text="You may do 50 more damage and leave your opponent's Active Pok\u00e9mon Paralyzed. If you do, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=_exavolt,
        ),
    ],
)