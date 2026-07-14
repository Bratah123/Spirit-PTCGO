from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.card_effects.support_common import search_to_bench, requires_bench_space
from spirit.game.session.effects import is_basic_pokemon


def _is_basic_lightning_or_dragon(card):
    if not is_basic_pokemon(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.LIGHTNING.value in types or PokemonTypes.DRAGON.value in types


STORMY_MOUNTAINS_ABILITY = Ability(
    title="Stormy Mountains",
    game_text="Once during each player's turn, that player may search their deck for a Basic Lightning Pokémon or Basic Dragon Pokémon and put it onto their Bench. Then, that player shuffles their deck.",
    activation=Activations.ONCE_PER_TURN,
    effect=search_to_bench(
        predicate=_is_basic_lightning_or_dragon,
        prompt="Choose a Basic Lightning or Dragon Pokémon to put onto your Bench.",
    ),
    condition=requires_bench_space(1),
)

card = StadiumCardDef(
    guid="8ce2028e-5116-55ad-9b4b-dc83f61e174d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StormyMountains.Name",
    display_name="Stormy Mountains",
    searchable_by=["Stormy Mountains", "Stadium"],
    subtypes=["Stadium"],
    collector_number=232,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    ability=STORMY_MOUNTAINS_ABILITY,
)
