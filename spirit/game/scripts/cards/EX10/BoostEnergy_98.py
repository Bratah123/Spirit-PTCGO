"""EX10 Unseen Forces — Boost Energy.
"""
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities
from spirit.game.card_effects.energies import discard_energy_end_of_turn
from spirit.game.card_effects.ex import boost_energy_lock_retreat
from spirit.game.session.effects import is_evolution_pokemon

_GUID = "a789f01f-a171-5d3e-a3c6-43a4649bdbb9"

card = EnergyCardDef(
    guid=_GUID,
    key="EX10",
    name="Boost Energy",
    display_name="Boost Energy",
    searchable_by=["Boost Energy", "Special"],
    subtypes=["Special"],
    collector_number=98,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
    attach_to=is_evolution_pokemon,
    passive=boost_energy_lock_retreat(),
    granted_abilities=[
        Ability(
            title="Boost Energy",
            game_text="Discard Boost Energy at the end of the turn it was attached.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=discard_energy_end_of_turn(_GUID),
        ),
    ],
)
