from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _flip_discard_defender_energy(ctx):
    """Printed damage; flip a coin. If heads, discard an Energy attached to
    your opponent's Active Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    target = ctx.opponent_active()
    if results and results[0] and target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard")


card = PokemonCardDef(
    guid="60a98c57-1fdf-51ec-84f3-0011b3e9fa49",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    display_name="Cacnea",
    searchable_by=["Cacnea", "Basic", "Cacnea"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=331,
    abilities=[
        Attack(
            title="Swagger",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_flip_discard_defender_energy,
        ),
    ],
)