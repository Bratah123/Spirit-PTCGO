from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def fortunate_eye(ctx):
    """Look at the top 5 cards of your opponent's deck and put them back in
    any order."""
    top = ctx.deck_top(5, ctx.opponent_id)
    if len(top) <= 1:
        return
    picked_ids = await ctx.session.prompt_card_chooser(
        ctx.player_id, ctx.source.entity_id, top, len(top), minimum=len(top),
        prompt="Put the cards back in any order.", ordered=True,
    )
    by_id = {c.entity_id: c for c in top}
    order = [by_id[i] for i in picked_ids if i in by_id]
    for card in top:
        if card not in order:
            order.append(card)
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    for card in order:
        deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)

card = PokemonCardDef(
    guid="9de00fec-28e5-5a73-a7cd-96cffa0f78d1",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    display_name="Gothita",
    searchable_by=["Gothita", "Basic", "Gothita"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=574,
    abilities=[
        Attack(
            title="Fortunate Eye",
            game_text="Look at the top 5 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fortunate_eye,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)