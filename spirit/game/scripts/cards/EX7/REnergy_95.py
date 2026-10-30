from spirit.game.card_effects.energies import discard_energy_end_of_turn
from spirit.game.card_effects.ex import REnergyPassive, r_energy_attach_to
from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities

_GUID = "118013fc-9de9-5215-bd40-6bfd7e48e008"

card = EnergyCardDef(
    guid="118013fc-9de9-5215-bd40-6bfd7e48e008",
    key="EX7",
    name="R Energy",
    display_name="R Energy",
    searchable_by=["R Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.DARKNESS, PokemonTypes.DARKNESS]],
    attach_to=r_energy_attach_to,
    passive=REnergyPassive(),
    granted_abilities=[
        Ability(
            title="R Energy",
            game_text="When your turn ends, discard R Energy.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.END_OF_TURN,
            effect=discard_energy_end_of_turn(_GUID),
        ),
    ],
)
