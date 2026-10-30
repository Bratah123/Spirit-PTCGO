"""STUB: effect not implemented — do not guess mechanics.
Blaziken (EX16 #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.ex import fire_stream_discard_spread, poke_power_condition
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard
from spirit.game.card_effects.trainers import player_has_bench


def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


def _firestarter_extra(board, player_id, pokemon):
    if not player_has_bench(board, player_id):
        return False
    return requires_discard(_is_fire_energy)(board, player_id, pokemon)


card = PokemonCardDef(
    guid="9ad3ce4f-5372-5a7b-9588-1b8c28243db1",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Ability(
            title="Firestarter",
            game_text="Once during your turn (before your attack), you may attach a Fire Energy card from your discard pile to 1 of your Benched Pok\u00e9mon. This power can't be used if Blaziken is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(_firestarter_extra),
            effect=attach_from_discard(predicate=_is_fire_energy, count=1, target=lambda pokemon: not is_in_active_spot(pokemon), prompt='Choose a Fire Energy card from your discard pile'),
        ),
        Attack(
            title="Fire Stream",
            game_text="Discard a Fire Energy card attached to Blaziken. This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=fire_stream_discard_spread(10),
        ),
    ],
)