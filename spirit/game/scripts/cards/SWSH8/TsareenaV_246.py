from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def queens_orders(ctx):
    """You may discard any number of your Benched Pokemon; this attack does
    40 more damage for each Benched Pokemon discarded this way."""
    bench = ctx.my_bench()
    picks = []
    if bench:
        picks = await ctx.choose_cards(
            bench, len(bench), minimum=0,
            prompt="Choose any number of your Benched Pokémon to discard.",
        )
    for pokemon in picks:
        await ctx.discard_cards(full_stack(pokemon))
    await ctx.deal_damage(20 + 40 * len(picks))


card = PokemonCardDef(
    guid="d0da8f96-8aab-548e-9d9d-0bcbb84a9089",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TsareenaV.Name",
    display_name="Tsareena V",
    searchable_by=["Tsareena V", "Basic", "V", "TsareenaV"],
    subtypes=["Basic", "V"],
    collector_number=246,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=763,
    abilities=[
        Attack(
            title="Queen's Orders",
            game_text="You may discard any number of your Benched Pok\u00e9mon. This attack does 40 more damage for each Benched Pok\u00e9mon you discarded in this way.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=queens_orders,
        ),
    ],
)