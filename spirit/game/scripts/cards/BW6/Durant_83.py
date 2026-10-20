from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def garbage_collection(ctx):
    """Put a card from your discard pile on top of your deck."""
    pile = list(ctx.discard_pile())
    if not pile:
        return
    picks = await ctx.choose_cards(
        pile, 1, prompt="Choose a card to put on top of your deck")
    if picks:
        await ctx.put_on_top_of_deck(picks[0])


card = PokemonCardDef(
    guid="4ec7aa8c-90ae-5cdd-821e-8416a35b2478",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=632,
    abilities=[
        Attack(
            title="Pull Out",
            game_text="Put a card from your discard pile on top of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=garbage_collection,
        ),
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)