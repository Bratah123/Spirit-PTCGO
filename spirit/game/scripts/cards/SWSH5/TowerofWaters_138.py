from spirit.game.data_utils import StadiumCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import retreat_discount

card = StadiumCardDef(
    guid="94bb45dd-7c82-57ef-ba64-f25f0a4c2e85",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TowerofWaters.Name",
    display_name="Tower of Waters",
    searchable_by=["Tower of Waters", "Stadium", "Rapid Strike"],
    subtypes=["Stadium", "Rapid Strike"],
    collector_number=138,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    passive=retreat_discount(
        2, target_pred=lambda p, c: "Rapid Strike" in subtypes_for(p.archetype_id)
    ),
)
