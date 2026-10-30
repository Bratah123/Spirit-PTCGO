"""Call Energy (DP5 #92)."""
from spirit.game.data_utils import EnergyCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, Rarities, AbilityTypes
from spirit.game.card_effects.energies import call_energy_ability, call_energy_ability_condition

card = EnergyCardDef(
    guid="c86675bb-9641-5053-a149-bb26dd9e6469", key="DP5", name="Call Energy", display_name="Call Energy",
    searchable_by=["Call Energy", "Special"], subtypes=["Special"],
    collector_number=92, set_code="DP5", rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS, is_special=True,
    granted_abilities=[
        Ability(
            title="Call Energy",
            game_text="Once during your turn, if the Pokémon Call Energy is attached to is your Active Pokémon, you may search your deck for up to 2 Basic Pokémon and put them onto your Bench. If you do, shuffle your deck and your turn ends.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=call_energy_ability,
            condition=call_energy_ability_condition,
        ),
    ],
)
