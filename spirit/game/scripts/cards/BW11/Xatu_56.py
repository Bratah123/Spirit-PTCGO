from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


_RPS = ["Rock", "Paper", "Scissors"]


async def _rps_winner(ctx):
    """Both players pick Rock/Paper/Scissors (replay ties); returns the
    winner's player id. Falls back to a coin flip after 5 ties."""
    for _ in range(5):
        mine = await ctx.choose("Rock-Paper-Scissors", _RPS, ctx.player_id, use_panel=False)
        theirs = await ctx.choose("Rock-Paper-Scissors", _RPS, ctx.opponent_id, use_panel=False)
        if mine != theirs:
            return ctx.player_id if (mine - theirs) % 3 == 1 else ctx.opponent_id
    heads = (await ctx.flip_coins(1, "Fortunate Draw"))[0]
    return ctx.player_id if heads else ctx.opponent_id


async def _fortunate_draw(ctx):
    """Rock-Paper-Scissors: the winner draws 3 cards, the loser discards the
    top 3 cards of their deck."""
    winner = await _rps_winner(ctx)
    loser = ctx.opponent_id if winner == ctx.player_id else ctx.player_id
    await ctx.draw_cards(3, player_id=winner)
    top = ctx.deck_top(3, player_id=loser)
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="c97fc9eb-8ec0-5d06-b4fd-c83ae8a7d1c8",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Attack(
            title="Fortunate Draw",
            game_text="You and your opponent play Rock-Paper-Scissors. The player who wins draws 3 cards. The player who loses discards the top 3 cards of his or her deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_fortunate_draw,
        ),
        Attack(
            title="Miracle Wing",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)