from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
import random


async def _chip_off(ctx):
    """Discard cards from your opponent's hand at random until they have 4."""
    hand = list(ctx.hand(ctx.opponent_id))
    if len(hand) > 4:
        await ctx.discard_cards(random.sample(hand, len(hand) - 4))


card = PokemonCardDef(
    guid="a475706b-1d67-5710-b70b-a206a523e941",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="XY2",
    rarity=Rarities.Rare,
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
            title="Chip Off",
            game_text="Discard cards from your opponent's hand at random until he or she has 4 cards in his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_chip_off,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)