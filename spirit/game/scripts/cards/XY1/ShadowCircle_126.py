from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.passives_common import no_weakness_passive
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.models.board import BoardState


def _has_darkness_energy(target, carrier):
    return any(energy_provides_type(e, PokemonTypes.DARKNESS.value)
               for e in BoardState.attached_energies(target))


card = StadiumCardDef(
    guid="afd45c1b-a248-5969-b353-fdc1f4061b38",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowCircle.Name",
    display_name="Shadow Circle",
    searchable_by=["Shadow Circle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=126,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=no_weakness_passive(protects=_has_darkness_energy)
)
