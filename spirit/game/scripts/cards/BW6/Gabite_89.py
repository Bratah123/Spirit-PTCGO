from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.session.effects import is_pokemon_card


def _deck_nonempty(board, player_id, pokemon=None):
    return deck_nonempty(board, player_id)


def _is_dragon_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.DRAGON.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="f01cea7e-03b2-5c74-9375-1af3aaae1d16",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=["Gabite", "Stage 1", "Gabite"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Ability(
            title="Dragon Call",
            game_text="Once during your turn (before your attack), you may search your deck for a Dragon Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_nonempty,
            effect=search_to_hand(_is_dragon_pokemon, count=1, minimum=0, reveal=True,
                                  prompt='Choose a Dragon Pok\u00e9mon to put into your hand.'),
        ),
        Attack(
            title="Dragonslice",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)