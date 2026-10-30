from spirit.game.card_effects.energies import (
    ALL_TYPES_TWO_AT_A_TIME,
    DoubleRainbowPassive,
    attach_to_evolved_non_ex,
    discard_energy_if_not_evolved,
)
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities

_GUID = "d2a27312-d2db-5b96-8be2-e2dd9a2f4674"

card = EnergyCardDef(
    guid="d2a27312-d2db-5b96-8be2-e2dd9a2f4674",
    key="POP5",
    name="Double Rainbow Energy",
    display_name="Double Rainbow Energy",
    searchable_by=["Double Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=4,
    set_code="POP5",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_TWO_AT_A_TIME,
    attach_to=attach_to_evolved_non_ex(),
    passive=DoubleRainbowPassive(),
    granted_abilities=[
        Ability(
            title="Double Rainbow Energy",
            game_text="When the Pokémon Double Rainbow Energy is attached to is no longer an Evolved Pokémon, discard Double Rainbow Energy.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=discard_energy_if_not_evolved(_GUID),
        ),
    ],
)
