from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


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
    guid="9701fb86-7c4a-5c4d-a9ae-3066a9c065dd",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1", "Noivern"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Tuning",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_synchrodraw,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)