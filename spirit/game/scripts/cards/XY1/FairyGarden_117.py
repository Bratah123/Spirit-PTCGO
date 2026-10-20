from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.models.board import BoardState


def _has_fairy_energy(pokemon, carrier):
    return any(energy_provides_type(e, PokemonTypes.FAIRY.value)
               for e in BoardState.attached_energies(pokemon))


card = StadiumCardDef(
    guid="3795d02e-1bd6-5a7f-8d79-c1b2548cd42d",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyGarden.Name",
    display_name="Fairy Garden",
    searchable_by=["Fairy Garden", "Stadium"],
    subtypes=["Stadium"],
    collector_number=117,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=retreat_free_when(_has_fairy_energy)
)
