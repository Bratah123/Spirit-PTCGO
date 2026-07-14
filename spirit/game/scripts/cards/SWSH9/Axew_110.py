from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


async def ultra_evolution(ctx):
    """Flip a coin; on heads, search a Haxorus and evolve this Axew with it."""
    heads = (await ctx.flip_coins(1, "Ultra Evolution"))[0]
    if not heads:
        return
    picks = await ctx.search_deck(
        lambda c: is_pokemon_card(c)
        and c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Haxorus",
        count=1, minimum=0,
        prompt="Choose a Haxorus to evolve this Axew.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.attacker, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="b2c9db6f-0a37-5c13-b147-5124b8e49527",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=610,
    abilities=[
        Attack(
            title="Ultra Evolution",
            game_text="Flip a coin. If heads, search your deck for a Haxorus and put it onto this Axew to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ultra_evolution,
        ),
    ],
)