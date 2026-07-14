from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import is_basic_pokemon


def _borne_ashore_candidates(board):
    candidates = []
    for pid in board.player_ids:
        bench = board.find_player_area(pid, "bench")
        if bench is None or len(bench.children) >= BENCH_CAPACITY:
            continue
        discard = board.find_player_area(pid, "discard")
        if discard:
            candidates.extend(c for c in discard.children if is_basic_pokemon(c))
    return candidates


def borne_ashore_condition(board, player_id, pokemon):
    return bool(_borne_ashore_candidates(board))


async def borne_ashore(ctx):
    """Put a Basic Pokémon from either player's discard pile onto that
    player's Bench."""
    candidates = _borne_ashore_candidates(ctx.board)
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from either discard pile to put onto that player's Bench.",
    )
    if not picks:
        return
    await ctx.bench_pokemon(picks[0])


card = PokemonCardDef(
    guid="18d77c2d-ac89-5d17-8cd7-45a2fcf6bcda",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name",
    display_name="Mantine",
    searchable_by=["Mantine", "Basic", "Mantine"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=226,
    abilities=[
        Attack(
            title="Borne Ashore",
            game_text="Put a Basic Pok\u00e9mon from either player's discard pile onto that player's Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            condition=borne_ashore_condition,
            effect=borne_ashore,
        ),
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)