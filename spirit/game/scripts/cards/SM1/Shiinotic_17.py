from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
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
    guid="dfd0ae6e-8e7f-5366-9695-00d5dac401e7",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiinotic.Name",
    display_name="Shiinotic",
    searchable_by=["Shiinotic", "Stage 1", "Shiinotic"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    family_id=755,
    abilities=[
        Ability(
            title="Illuminate",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_illuminate_condition,
            effect=search_to_hand(_is_grass_pokemon, count=1, minimum=0, reveal=True, prompt='Choose a Grass Pokémon to put into your hand.'),
        ),
        Attack(
            title="Flickering Spores",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)