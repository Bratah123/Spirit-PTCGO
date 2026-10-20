from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.session.passives import Passive, ability_locked
from spirit.game.session.effects import is_basic_pokemon


class UnobservantPassive(Passive):
    """Marker for Unobservant; the restriction itself lives in
    _unobservant_allows, the condition= gate on this card's attacks."""


def _unobservant_allows(board, player_id, pokemon):
    """Unobservant: if the opponent's Active is a Basic Pokemon this Pokemon
    can't attack (unless its Ability is turned off)."""
    if ability_locked(board, pokemon):
        return True
    for pid in board.player_ids:
        if pid != player_id:
            active = board.active_pokemon(pid)
            return active is None or not is_basic_pokemon(active)
    return True


card = PokemonCardDef(
    guid="2fd74bde-49cd-5446-8e28-7e9622c4f0be",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Unobservant",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this Pok\u00e9mon can't attack.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=UnobservantPassive(),
        ),
        Attack(
            title="Crushing Blow",
            game_text="Discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=discard_opponent_energy_attack(),
            condition=_unobservant_allows,
        ),
    ],
)