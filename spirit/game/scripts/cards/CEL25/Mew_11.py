from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card
from spirit.game.card_effects.pokemon import in_active_spot


async def mysterious_tail(ctx):
    """You may look at the top 6 cards of your deck, reveal an Item card you
    find there, and put it into your hand. Shuffle the rest back."""
    if not await ctx.ask_yes_no("Look at the top 6 cards of your deck?"):
        return
    top = ctx.deck_top(6)
    candidates = [c for c in top if is_item_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose an Item card to put into your hand.",
        display_cards=top,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="637c92b7-bbaa-5279-b62d-0dc204ee4e6c",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="CEL25",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=151,
    abilities=[
        Ability(
            title="Mysterious Tail",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 6 cards of your deck, reveal an Item card you find there, and put it into your hand. Shuffle the other cards back into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=mysterious_tail,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)