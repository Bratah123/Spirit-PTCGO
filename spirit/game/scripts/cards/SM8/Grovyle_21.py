from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.attributes import AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_pokemon_card

def _is_grass_pokemon(card):
    return is_pokemon_card(card) and \
        PokemonTypes.GRASS.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])

def _illuminate_condition(board, player_id, pokemon=None):
    return deck_nonempty(board, player_id)

card = PokemonCardDef(
    guid="8ce40b7e-419f-57a6-8624-87a08c2a3a7a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    display_name="Grovyle",
    searchable_by=["Grovyle", "Stage 1", "Grovyle"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name",
    family_id=252,
    abilities=[
        Ability(
            title="Sunshine Grace",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_illuminate_condition,
            effect=search_to_hand(_is_grass_pokemon, count=1, minimum=0, reveal=True, prompt='Choose a Grass Pokémon to put into your hand.'),
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
        ),
    ],
)