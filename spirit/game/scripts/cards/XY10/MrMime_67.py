from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _synchrodraw(ctx):
    """Shuffle your hand into your deck, then draw as many cards as your
    opponent has in hand."""
    count = ctx.hand_size(ctx.opponent_id)
    hand = list(ctx.hand())
    if hand:
        await ctx.shuffle_into_deck(hand)
    else:
        await ctx.shuffle_deck()
    if count > 0:
        await ctx.draw_cards(count)


card = PokemonCardDef(
    guid="909a77d7-4fe9-5149-bcb2-c2af1972ac3f",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=122,
    abilities=[
        Attack(
            title="Mimic",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_synchrodraw,
        ),
        Attack(
            title="Juggling",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)