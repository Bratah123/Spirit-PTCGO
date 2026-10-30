from spirit.game.data_utils import Ability, EnergyCardDef, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, Rarities
from spirit.game.card_effects.energies import discard_energy_if_not_evolved
from spirit.game.card_effects.ex import scramble_energy_attach_to, scramble_energy_passive

card = EnergyCardDef(
    guid="4efc5f1e-deba-5ca4-90d2-87e9f17147b6",
    key="EX15",
    name="Scramble Energy",
    display_name="Scramble Energy",
    searchable_by=["Scramble Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS]],
    attach_to=scramble_energy_attach_to,
    passive=scramble_energy_passive(),
    granted_abilities=[
        Ability(
            title="Scramble Energy",
            game_text="If the Pokémon Scramble Energy is attached to isn't an Evolved Pokémon (or evolves into Pokémon-ex), discard Scramble Energy.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=discard_energy_if_not_evolved(
                "5fba8084-7296-5ddc-b42b-c24c7454d384"),
        ),
    ],
)
