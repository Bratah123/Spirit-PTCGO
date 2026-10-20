from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import no_resistance_passive

card = StadiumCardDef(
    guid="9148c756-7b30-5ce2-ba36-3ffac496e77e",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagneticStorm.Name",
    display_name="Magnetic Storm",
    searchable_by=["Magnetic Storm", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    passive=no_resistance_passive(when=lambda calc, carrier: True)
)
