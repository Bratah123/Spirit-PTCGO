from spirit.game.card_effects.energies import (
    attach_to_team_name,
    discard_energy_end_of_turn,
)
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities

_GUID = "09dd569f-37fa-567a-8b4e-662d8927d9e9"

card = EnergyCardDef(
    guid="09dd569f-37fa-567a-8b4e-662d8927d9e9",
    key="EX4",
    name="Aqua Energy",
    display_name="Aqua Energy",
    searchable_by=["Aqua Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[
        [PokemonTypes.WATER, PokemonTypes.WATER],
        [PokemonTypes.DARKNESS, PokemonTypes.DARKNESS],
        [PokemonTypes.WATER, PokemonTypes.DARKNESS],
    ],
    attach_to=attach_to_team_name("Team Aqua"),
    granted_abilities=[
        Ability(
            title="Aqua Energy",
            game_text="At the end of your turn, discard Aqua Energy.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=discard_energy_end_of_turn(_GUID),
        ),
    ],
)
