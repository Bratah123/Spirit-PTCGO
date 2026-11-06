from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive
from spirit.game.session.effects import plasma_energy_attached


class PlasmaFrigatePassive(Passive):
    """Each Pokemon that has any Plasma Energy attached (both sides) has no Weakness."""

    def modify_weakness(self, calc, carrier):
        if calc.target is not None and plasma_energy_attached(calc.target):
            calc.weakness_applies = False


card = StadiumCardDef(
    guid="892bd555-cbe9-5221-b731-11585b08773b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlasmaFrigate.Name",
    display_name="Plasma Frigate",
    searchable_by=["Plasma Frigate", "Stadium", "Team Plasma"],
    subtypes=["Stadium", "Team Plasma"],
    collector_number=124,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    passive=PlasmaFrigatePassive()
)
