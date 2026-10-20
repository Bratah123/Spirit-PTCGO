from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _supporter_played_this_turn(ctx):
    return ctx.supporters_played_this_turn() > 0


def _premonition_condition(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def _premonition(ctx):
    """Look at the top 5 cards of your deck and put them back in any order."""
    top = ctx.deck_top(5)
    if not top:
        return
    order = await ctx.choose_cards(top, len(top), minimum=len(top), ordered=True, display_cards=top,
                                   prompt="Choose the order (first = top)") or top
    for card in reversed(list(order)):
        await ctx.put_on_top_of_deck(card)


card = PokemonCardDef(
    guid="ba2c578b-b8c8-52ce-8bd9-23f717ff7ab3",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gallade.Name",
    display_name="Gallade",
    searchable_by=["Gallade", "Stage 2", "Gallade"],
    subtypes=["Stage 2"],
    collector_number=84,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Premonition",
            game_text="Once during your turn (before your attack), you may look at the top 5 cards of your deck and put them back on top of your deck in any order.",
            activation=Activations.ONCE_PER_TURN,
            condition=_premonition_condition,
            effect=_premonition,
        ),
        Attack(
            title="Sensitive Blade",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_supporter_played_this_turn, 70),
        ),
    ],
)