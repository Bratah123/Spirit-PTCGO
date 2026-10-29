from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.support_common import remove_self_from_play


def _cowardice_condition(board, player_id, pokemon=None):
    state = getattr(board, "turn_state", None)
    if state is None or pokemon is None or state.turn_number <= 2:
        return False  # not during your first turn
    return state.entered_play_turn.get(pokemon.entity_id, 0) < state.turn_number


card = PokemonCardDef(
    guid="c92aeed8-b72c-5f7c-b8e4-e9b21492e29b",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=746,
    abilities=[
        Ability(
            title="Cowardice",
            game_text="Once during your turn (before your attack), you may discard all cards attached to this Pok\u00e9mon and return it to your hand. You can't use this Ability during your first turn or on the turn this Pok\u00e9mon was put into play.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_cowardice_condition,
            effect=remove_self_from_play('hand', with_attachments='discard'),
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)