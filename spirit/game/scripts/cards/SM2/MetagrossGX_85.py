from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.pokemon import energy_provides_type, is_energy_card
from spirit.game.card_effects.support_common import attach_from_discard, search_to_hand
from spirit.game.data_utils import Activations
from spirit.game.attributes import AttrID as _A
from spirit.game.card_effects.passives_common import is_in_active_spot


def _psychic_or_metal_energy(card):
    return is_energy_card(card) and (
        energy_provides_type(card, PokemonTypes.PSYCHIC.value)
        or energy_provides_type(card, PokemonTypes.METAL.value)
    )


def _is_active_pokemon(pokemon):
    parent = pokemon.parent
    return bool(parent) and parent.get_attribute(_A.NAME) == "activePokemonArea"


def geotech_condition(board, player_id, pokemon=None):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_psychic_or_metal_energy(c) for c in discard.children)


geotech_system = attach_from_discard(
    _psychic_or_metal_energy, count=1, target=_is_active_pokemon, minimum=1,
    prompt="Choose a Psychic or Metal Energy card to attach to your Active Pokémon",
)
algorithm_gx = search_to_hand(None, count=5, minimum=0, reveal=False,
                              prompt="Choose up to 5 cards to put into your hand")


card = PokemonCardDef(
    guid="8a49fc1b-23a3-53e6-8763-6d0238da3fe3",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossGX.Name",
    display_name="Metagross-GX",
    searchable_by=["Metagross-GX", "Stage 2", "GX", "MetagrossGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=85,
    set_code="SM2",
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Geotech System",
            game_text="Once during your turn (before your attack), you may attach a Psychic or Metal Energy card from your discard pile to your Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN, condition=geotech_condition,
            effect=geotech_system,
        ),
        Attack(
            title="Giga Hammer",
            game_text="This Pok\u00e9mon can't use Giga Hammer during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            locks_next_turn=True,
            effect=None,
        ),
        Attack(
            title="Algorithm-GX",
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=algorithm_gx,
        ),
    ],
)