from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _power_pinch(ctx):
    """Flip 2 coins. For each heads, discard an Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Power Pinch")
    heads = sum(1 for r in results if r)
    defender = ctx.defender
    if not heads or defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, heads, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="82d84d24-e57d-5d14-a54e-613d3618cb79",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MMawileEX.Name",
    display_name="M Mawile-EX",
    searchable_by=["M Mawile-EX", "MEGA", "EX", "MMawileEX"],
    subtypes=["MEGA", "EX"],
    collector_number=104,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MawileEX.Name",
    family_id=303,
    abilities=[
        Attack(
            title="Twin Grapple",
            game_text="Flip 2 coins. For each heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 3},
            damage=130,
            effect=_power_pinch,
        ),
    ],
)