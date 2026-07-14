from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def future_sight(ctx):
    """Look at the top 4 cards of either player's deck, put back in any order."""
    choice = await ctx.choose(
        "Look at the top 4 cards of which deck?",
        ["Your deck", "Opponent's deck"], use_panel=False,
    )
    target_pid = ctx.player_id if choice == 0 else ctx.opponent_id
    top = ctx.deck_top(4, target_pid)
    if len(top) <= 1:
        return
    order = await ctx.choose_cards(
        top, len(top), minimum=len(top), ordered=True, player_id=ctx.player_id,
        prompt="Put the cards back in any order",
    )
    if not order:
        order = top
    deck = ctx.board.find_player_area(target_pid, "deck")
    for card in order:
        if card in deck.children:
            deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)


card = PokemonCardDef(
    guid="0f25213f-8b0b-555e-85de-1bb672a225a4",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=337,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 4 cards of either player's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=future_sight,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 20 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 20, base=20),
        ),
    ],
)