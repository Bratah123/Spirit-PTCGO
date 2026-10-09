from spirit.game.card_effects.energies import ALL_TYPES_ONE_AT_A_TIME
from spirit.game.data_utils import EnergyCardDef, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


def _fusion_strike_carrier(pokemon) -> bool:
    """Official: only attachable to a Fusion Strike Pok\u00e9mon (anything
    else would discard this card)."""
    return "Fusion Strike" in subtypes_for(
        getattr(pokemon, "archetype_id", None))


class FusionStrikeShieldPassive(Passive):
    """Prevent all effects of your opponent's Pok\u00e9mon's Abilities done
    to the Pok\u00e9mon this card is attached to."""

    def blocks_ability_effects(self, target, carrier):
        return target is carrier_pokemon(carrier)


card = EnergyCardDef(
    guid="a1be9557-4439-5c31-8c90-51a75824090f",
    key="SWSH8",
    name="Fusion Strike Energy",
    display_name="Fusion Strike Energy",
    searchable_by=["Fusion Strike Energy", "Fusion Strike", "Special"],
    subtypes=["Fusion Strike", "Special"],
    collector_number=244,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    attach_to=_fusion_strike_carrier,
    passive=FusionStrikeShieldPassive(),
)
