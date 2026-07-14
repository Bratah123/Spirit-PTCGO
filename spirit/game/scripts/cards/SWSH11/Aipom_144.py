from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mischievous_tail(ctx):
    """Look at the top card of your opponent's deck. You may have your
    opponent shuffle their deck."""
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if top:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, top,
            prompt="Top card of your opponent's deck",
        )
    if await ctx.ask_yes_no("Have your opponent shuffle their deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)


card = PokemonCardDef(
    guid="37870c3e-4161-59bd-80c0-6612f507fbf9",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Mischievous Tail",
            game_text="Look at the top card of your opponent's deck. You may have your opponent shuffle their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mischievous_tail,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)