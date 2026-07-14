from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def frozen_awakening(ctx):
    """Search your deck for a card that evolves from this Pokemon and evolve it. Then shuffle."""
    logic_name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda c: logic_name and c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic_name,
        count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


async def heavy_snow(ctx):
    """120. Discard a Stadium in play."""
    await ctx.deal_damage()
    await ctx.discard_stadium()


card = PokemonCardDef(
    guid="98dc82c0-94b0-59d2-86a4-2bef8247dfb1",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    display_name="Glaceon V",
    searchable_by=["Glaceon V", "Basic", "V", "GlaceonV"],
    subtypes=["Basic", "V"],
    collector_number=175,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=471,
    abilities=[
        Attack(
            title="Frozen Awakening",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=frozen_awakening,
        ),
        Attack(
            title="Heavy Snow",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=heavy_snow,
        ),
    ],
)