from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.card_effects.trainers import bench_has_room
from spirit.game.session.effects import is_basic_pokemon


def _is_basic_water_or_fighting(card):
    if not is_basic_pokemon(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.WATER.value in types or PokemonTypes.FIGHTING.value in types


def _brooklet_condition(board, player_id, pokemon=None):
    return bench_has_room(board, player_id)


BROOKLET_HILL_ABILITY = Ability(
    title="Brooklet Hill",
    game_text="Once during each player's turn, that player may search their deck for a Basic Water Pokémon or Basic Fighting Pokémon and put it onto their Bench. Then, that player shuffles their deck.",
    activation=Activations.ONCE_PER_TURN,
    condition=_brooklet_condition,
    effect=search_to_bench(
        _is_basic_water_or_fighting, count=1,
        prompt="Choose a Basic Water or Basic Fighting Pokémon to put onto your Bench.",
    ),
)

card = StadiumCardDef(
    guid="5f7cfa81-4439-597b-b8fa-e4ac46729c22",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrookletHill.Name",
    display_name="Brooklet Hill",
    searchable_by=["Brooklet Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=120,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    ability=BROOKLET_HILL_ABILITY,
)
