from spirit.game.card_effects.trainers import adaman, has_two_metal_energy_in_hand
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="17b6ab8f-f7a2-53dc-ae08-f44b6e76ca5a",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Adaman.Name",
    display_name="Adaman",
    searchable_by=["Adaman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=199,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=adaman,
    condition=has_two_metal_energy_in_hand
)
