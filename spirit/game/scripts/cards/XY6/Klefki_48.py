from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.effects import is_item_card


async def _look_for_keys(ctx):
    """Reveal from the top until an Item card; put it into your hand; shuffle."""
    deck = list(reversed(ctx.deck()))
    revealed = []
    item = None
    for card in deck:
        revealed.append(card)
        if is_item_card(card):
            item = card
            break
    if revealed:
        await ctx.reveal_cards(revealed)
    if item is not None:
        await ctx.put_in_hand([item], reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="aa8eb436-ae05-5ba1-ac2c-a05c30e65b15",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Attack(
            title="Look for Keys",
            game_text="Reveal cards from the top of your deck until you reveal an Item card. Put it into your hand. Shuffle the other cards back into your deck.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_look_for_keys,
        ),
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)