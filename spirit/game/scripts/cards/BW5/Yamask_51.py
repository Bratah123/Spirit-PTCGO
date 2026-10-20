from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
import random


async def _astonish(ctx):
    """Printed damage; flip, heads a random card from the opponent's hand is
    revealed and shuffled into their deck."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Astonish")
    hand = list(ctx.hand(ctx.opponent_id))
    if not results or not results[0] or not hand:
        return
    pick = random.choice(hand)
    await ctx.reveal_cards([pick])
    await ctx.shuffle_into_deck([pick], ctx.opponent_id)


card = PokemonCardDef(
    guid="fa49bbf0-251c-52b4-9898-f23f860b3b97",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=562,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a card at random from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_astonish,
        ),
    ],
)