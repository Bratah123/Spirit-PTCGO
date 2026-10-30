from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive


class AltaroftheMoonePassive(Passive):
    """Retreat cost -2 for any Pokemon with Psychic or Darkness Energy attached."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        for child in pokemon.children:
            if energy_provides_type(child, PokemonTypes.PSYCHIC.value) \
                    or energy_provides_type(child, PokemonTypes.DARKNESS.value):
                return max(0, cost - 2)
        return cost


card = StadiumCardDef(
    guid="b1d91432-5568-55f2-bd79-723bd0422afe",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AltaroftheMoone.Name",
    display_name="Altar of the Moone",
    searchable_by=["Altar of the Moone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=AltaroftheMoonePassive(),
)
