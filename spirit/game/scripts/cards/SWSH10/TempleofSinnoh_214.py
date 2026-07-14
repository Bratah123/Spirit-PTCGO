from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class TempleOfSinnohPassive(Passive):
    """All Special Energy (both players') provide only Colorless Energy."""

    def suppresses_special_energy(self, energy, carrier) -> bool:
        return True


card = StadiumCardDef(
    guid="c7bb055b-6045-5562-b0f6-de5998fade2e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TempleofSinnoh.Name",
    display_name="Temple of Sinnoh",
    searchable_by=["Temple of Sinnoh", "Stadium"],
    subtypes=["Stadium"],
    collector_number=214,
    set_code="SWSH10",
    rarity=Rarities.RareSecret,
    passive=TempleOfSinnohPassive(),
)
