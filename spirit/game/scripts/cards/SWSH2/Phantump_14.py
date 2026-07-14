from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.constants import BENCH_CAPACITY


async def dark_guidance(ctx):
    """Put a Basic Pokemon from your discard pile onto your Bench."""
    if len(ctx.my_bench()) >= BENCH_CAPACITY:
        return
    candidates = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your discard pile to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="2962aa46-1df3-55e3-91be-1b88f5f31e72",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic", "Phantump"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=708,
    abilities=[
        Attack(
            title="Dark Guidance",
            game_text="Put a Basic Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=dark_guidance,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)