from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.pokemon import in_active_spot


async def ocean_search(ctx):
    """You may look at the top 6 cards of your deck, reveal a Pokemon you
    find there, and put it into your hand. Shuffle the rest back."""
    if not await ctx.ask_yes_no("Look at the top 6 cards of your deck?"):
        return
    top = ctx.deck_top(6)
    candidates = [c for c in top if is_pokemon_card(c)]
    picks = []
    if candidates:
        picks = await ctx.choose_cards(
            candidates, 1, minimum=0,
            prompt="Choose a Pokémon to put into your hand.",
            display_cards=top,
        )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="e03d7ce7-cff1-5074-b980-7b57d8884816",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SWSH45",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Ability(
            title="Ocean Search",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may look at the top 6 cards of your deck, reveal a Pok\u00e9mon you find there, and put it into your hand. Shuffle the other cards back into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=ocean_search,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)