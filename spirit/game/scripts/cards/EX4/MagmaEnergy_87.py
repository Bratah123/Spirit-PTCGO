from spirit.game.card_effects.energies import (
    attach_to_team_name,
    discard_energy_end_of_turn,
)
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities

_GUID = "d39dd7f6-5354-535d-9c96-836c92be088a"

card = EnergyCardDef(
    guid="d39dd7f6-5354-535d-9c96-836c92be088a",
    key="EX4",
    name="Magma Energy",
    display_name="Magma Energy",
    searchable_by=["Magma Energy", "Special"],
    subtypes=["Special"],
    collector_number=87,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # Fighting and/or Darkness, 2 Energy at a time
    provides=[
        [PokemonTypes.FIGHTING, PokemonTypes.FIGHTING],
        [PokemonTypes.DARKNESS, PokemonTypes.DARKNESS],
        [PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    ],
    attach_to=attach_to_team_name("Team Magma"),
    granted_abilities=[
        Ability(
            title="Magma Energy",
            game_text="At the end of your turn, discard Magma Energy.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=discard_energy_end_of_turn(_GUID),
        ),
    ],
)
