from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait


async def _future_spin(ctx):
    """Look at the top 3 cards of either player's deck and put them back in any order."""
    pid = ctx.opponent_id if await ctx.ask_yes_no("Look at your opponent's deck? (No = your own)") else ctx.player_id
    top = ctx.deck_top(3, pid)
    if not top:
        return
    order = await ctx.choose_cards(top, len(top), minimum=len(top), ordered=True, display_cards=top,
                                   prompt="Choose the order (first = top)") or top
    for card in reversed(list(order)):
        await ctx.put_on_top_of_deck(card)


card = PokemonCardDef(
    guid="df3c3948-bbbe-5a99-851a-48364afb9c49",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    display_name="Baltoy",
    searchable_by=["Baltoy", "Basic", "Baltoy"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="XY7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=343,
    abilities=[
        ancient_trait('θ Stop'),
        Attack(
            title="Future Spin",
            game_text="Look at the top 3 cards of either player's deck and put them back on top of that player's deck in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_future_spin,
        ),
    ],
)