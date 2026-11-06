from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon

# Same shape as Neo Upper Energy: every type, two of that type at a time.
ALL_TYPES_TWO_AT_A_TIME = [
    [option[0].value, option[0].value] for option in ALL_TYPES_ONE_AT_A_TIME
]


def _is_dragon(pokemon) -> bool:
    return PokemonTypes.DRAGON.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


class DoubleDragonPassive(Passive):
    """On a Dragon Pokémon: every type of Energy, 2 at a time.

    Card also says discard if attached to a non-Dragon. Attachment is gated by
    attach_to; mid-game type loss discard is not scripted here.
    """

    def modify_energy_provided(self, options, energy, holder, board):
        if carrier_pokemon(energy) is not holder or holder is None:
            return options
        if not _is_dragon(holder):
            return options
        return [list(opt) for opt in ALL_TYPES_TWO_AT_A_TIME]


card = EnergyCardDef(
    guid="2f0c1f4b-b09c-5cb4-9a43-a19803ede03e",
    key="XY6",
    name="Double Dragon Energy",
    display_name="Double Dragon Energy",
    searchable_by=["Double Dragon Energy", "Special"],
    subtypes=["Special"],
    collector_number=97,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    attach_to=_is_dragon,
    provides=[[PokemonTypes.COLORLESS]],
    passive=DoubleDragonPassive(),
)
