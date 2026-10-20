from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _mine(ctx):
    """Look at the top card of your opponent's deck; you may have them shuffle."""
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if top:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, top,
            prompt="Top card of your opponent's deck",
        )
    if await ctx.ask_yes_no("Have your opponent shuffle their deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)


card = PokemonCardDef(
    guid="69167ea7-b5cc-5c28-8809-c8b1e50242f5",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic", "Diglett"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Mine",
            game_text="Look at the top card of your opponent's deck. Then, you may have your opponent shuffle his or her deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=_mine,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)