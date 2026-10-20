from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _astonish(ctx):
    """Flip a coin. If heads, choose a random card from your opponent's hand;
    they reveal it and shuffle it into their deck."""
    import random
    results = await ctx.flip_coins(1, ctx.ability.title)
    hand = ctx.hand(ctx.opponent_id)
    if not results or not results[0] or not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.shuffle_into_deck([card], ctx.opponent_id)


card = PokemonCardDef(
    guid="be2644f6-436b-505f-9026-47c83eec4e16",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic", "Foongus"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=590,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_astonish,
        ),
    ],
)