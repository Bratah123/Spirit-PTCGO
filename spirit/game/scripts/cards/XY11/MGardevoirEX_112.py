from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def _despair_ray(ctx):
    """Discard as many of your Benched Pokemon as you like; +10 each."""
    bench = ctx.my_bench()
    picked = await ctx.choose_cards(bench, len(bench), minimum=0,
                                    prompt="Discard any of your Benched Pokémon") if bench else []
    for p in picked:
        await ctx.discard_cards(full_stack(p))
    await ctx.deal_damage(110 + 10 * len(picked))


card = PokemonCardDef(
    guid="187d88d4-f2bf-5f58-8dec-1765979e0418",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name",
    display_name="M Gardevoir-EX",
    searchable_by=["M Gardevoir-EX", "MEGA", "EX", "MGardevoirEX"],
    subtypes=["MEGA", "EX"],
    collector_number=112,
    set_code="XY11",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.FAIRY, PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Despair Ray",
            game_text="Discard as many of your Benched Pok\u00e9mon as you like. This attack does 10 more damage for each Benched Pok\u00e9mon you discarded in this way.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator="+",
            effect=_despair_ray,
        ),
    ],
)