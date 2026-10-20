from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_restored_pokemon, effective_bench_capacity


def _beam_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and (bench is None or len(bench.children) < effective_bench_capacity(board, player_id))


card = PokemonCardDef(
    guid="c70b49f7-5ea2-51ff-ac54-854a2822e57e",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 1", "Omastar"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Restoring Beam",
            game_text="Once during your turn (before your attack), you may search your deck for a Restored Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            activation=Activations.ONCE_PER_TURN,
            condition=_beam_condition,
            effect=search_to_bench(is_restored_pokemon, 1, prompt="Choose a Restored Pokémon"),
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)