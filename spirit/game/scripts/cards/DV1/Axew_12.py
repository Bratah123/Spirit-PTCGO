from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card


async def signs_of_evolution(ctx):
    """Flip a coin. If heads, search deck for Fraxure into hand."""
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    picks = await ctx.search_deck(
        lambda c: is_pokemon_card(c)
        and c.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Fraxure",
        count=1, minimum=0,
        prompt="Choose a Fraxure to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="eb34c9f5-938a-5ca7-87d6-416e8b969318",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="DV1",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=610,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Flip a coin. If heads, search your deck for Fraxure, reveal it, and put it into your hand, Shuffle your deck afterward.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=signs_of_evolution,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)
