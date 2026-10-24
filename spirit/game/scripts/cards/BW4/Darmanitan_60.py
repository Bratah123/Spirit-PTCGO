from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, count_energy


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
    guid="42758e19-f82c-57be-90a3-681fe55469ef",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Synchrodraw",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_synchrodraw,
        ),
        Attack(
            title="DarMAXitan",
            game_text="Flip a coin for each Energy attached to this Pok\u00e9mon. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy(), per_heads=50),
        ),
    ],
)