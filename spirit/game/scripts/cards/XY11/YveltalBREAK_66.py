from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _unwavering_blade(ctx):
    """110; 30 to each of your opponent's damaged Benched Pokemon."""
    await ctx.deal_damage()
    for p in ctx.opponent_bench():
        if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0):
            await ctx.deal_damage(30, target=p)


card = PokemonCardDef(
    guid="c8652a62-42ce-5693-a6f9-f2dae1b2824a",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.YveltalBREAK.Name",
    display_name="Yveltal BREAK",
    searchable_by=["Yveltal BREAK", "BREAK", "YveltalBREAK"],
    subtypes=["BREAK"],
    collector_number=66,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    family_id=717,
    abilities=[
        Attack(
            title="Baleful Night",
            game_text="This attack does 30 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 3},
            damage=120,
            effect=_unwavering_blade,
        ),
    ],
)