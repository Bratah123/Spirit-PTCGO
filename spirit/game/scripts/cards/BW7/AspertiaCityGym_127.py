from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import Passive


class AspertiaCityGymPassive(Passive):
    """Each Colorless Pok\u00e9mon in play (both sides) gets +20 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
        return 20 if PokemonTypes.COLORLESS.value in types else 0


card = StadiumCardDef(
    guid="325e1feb-7c9c-53cc-bb9a-290e604ea12c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AspertiaCityGym.Name",
    display_name="Aspertia City Gym",
    searchable_by=["Aspertia City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    passive=AspertiaCityGymPassive()
)
