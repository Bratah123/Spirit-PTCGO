from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
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
    guid="7bab3d24-415f-55b6-8b86-01ab74979be9",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=355,
    abilities=[
        Attack(
            title="Dark Guidance",
            game_text="Put a Basic Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=dark_guidance,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
