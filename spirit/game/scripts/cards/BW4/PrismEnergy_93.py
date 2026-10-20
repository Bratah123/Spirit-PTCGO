from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import Passive, active_passives, special_energy_suppressed


_ALL_TYPES = [[t.value for t in option] for option in ALL_TYPES_ONE_AT_A_TIME]


class PrismEnergyPassive(Passive):
    """Provides Colorless; attached to a Basic Pokemon it provides every type
    of Energy, but only 1 Energy at a time."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or not is_basic_pokemon(holder):
            return options
        if special_energy_suppressed(board, energy):
            return options
        for passive, carrier in active_passives(board):
            if isinstance(passive, PrismEnergyPassive) and carrier is energy:
                return [list(option) for option in _ALL_TYPES]
        return options


card = EnergyCardDef(
    guid="9c230178-86f2-5924-b042-09f1fa7e0ac2",
    key="BW4",
    name="Prism Energy",
    display_name="Prism Energy",
    searchable_by=["Prism Energy", "Special"],
    subtypes=["Special"],
    collector_number=93,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    passive=PrismEnergyPassive(),
)
