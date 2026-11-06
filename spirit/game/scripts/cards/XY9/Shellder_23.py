from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _clamp(ctx):
    """30; flip: heads Paralyzed; tails this attack does nothing."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]):
        return
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="993cfffa-fedf-54af-a823-2b01b79abb8b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    display_name="Shellder",
    searchable_by=["Shellder", "Basic", "Shellder"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=90,
    abilities=[
        Attack(
            title="Clamp",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_clamp,
        ),
    ],
)