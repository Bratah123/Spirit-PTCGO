from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.passives import Passive


class _ForestOfGiantPlants(Passive):
    """Each player's Grass Pokemon can evolve during his or her first turn or
    the turn he or she plays those Pokemon."""
    def may_evolve_early(self, pokemon, carrier):
        return PokemonTypes.GRASS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = StadiumCardDef(
    guid="aedb9e18-b3de-5561-a0ba-57491ab1a270",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestofGiantPlants.Name",
    display_name="Forest of Giant Plants",
    searchable_by=["Forest of Giant Plants", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    passive=_ForestOfGiantPlants()
)
