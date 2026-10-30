from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import energy_removal
from spirit.game.card_effects.trainers import opponent_has_energy_attached


card = ItemCardDef(
    guid="445c272e-28dd-5f7a-aaeb-ac6bd41aa74d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval.Name",
    display_name="Energy Removal",
    searchable_by=["Energy Removal"],
    subtypes=[],
    collector_number=119,
    set_code="BASE4",
    rarity=Rarities.Common,
    condition=opponent_has_energy_attached,
    effect=energy_removal,
)
