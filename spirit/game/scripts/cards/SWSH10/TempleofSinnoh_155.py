from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class TempleOfSinnohPassive(Passive):
    """All Special Energy (both players') provide only Colorless Energy."""

    def suppresses_special_energy(self, energy, carrier) -> bool:
        return True


card = StadiumCardDef(
    guid="a2fd5726-8e67-5bd1-af21-1a6e3705abc4",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TempleofSinnoh.Name",
    display_name="Temple of Sinnoh",
    searchable_by=["Temple of Sinnoh", "Stadium"],
    subtypes=["Stadium"],
    collector_number=155,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    passive=TempleOfSinnohPassive(),
)
