from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.session.effects import is_basic_pokemon


async def _revival(ctx):
    """Put a Basic Pokemon from your opponent's discard pile onto their Bench."""
    cards = [c for c in ctx.discard_pile(ctx.opponent_id) if is_basic_pokemon(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Basic Pokémon")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = PokemonCardDef(
    guid="a1033261-4a71-5215-bea4-3b9eb2eacec7",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=355,
    abilities=[
        Attack(
            title="Revival",
            game_text="Put a Basic Pok\u00e9mon from your opponent's discard pile onto his or her Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_revival,
        ),
        Attack(
            title="Sneaky Placement",
            game_text="Put 1 damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(1, 'opponent_active'),
        ),
    ],
)