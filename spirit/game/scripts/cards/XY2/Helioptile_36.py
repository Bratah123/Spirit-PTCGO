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
    guid="11095e66-5047-5b3b-a1dd-9293122bd3df",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    display_name="Helioptile",
    searchable_by=["Helioptile", "Basic", "Helioptile"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=694,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title="Destructive Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=_flip_discard_defender_energy,
        ),
    ],
)