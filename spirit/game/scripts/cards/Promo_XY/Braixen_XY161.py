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
    guid="096d9b80-9bf8-5f8e-9b4d-73fb86ce9a83",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    display_name="Braixen",
    searchable_by=["Braixen", "Stage 1", "Braixen"],
    subtypes=["Stage 1"],
    collector_number=161,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Destructive Flame",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=_flip_discard_defender_energy,
        ),
        Attack(
            title="Crackling Ribbon",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)