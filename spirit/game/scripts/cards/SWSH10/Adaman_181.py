from spirit.game.card_effects.trainers import adaman, has_two_metal_energy_in_hand
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="07e5bc6b-0da5-5fe8-92cc-e7be35c2e1ec",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Adaman.Name",
    display_name="Adaman",
    searchable_by=["Adaman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=adaman,
    condition=has_two_metal_energy_in_hand
)
