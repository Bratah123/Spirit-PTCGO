from spirit.game.card_effects.trainers import adaman, has_two_metal_energy_in_hand
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="128f0ded-5b9e-5311-bf72-ca5a02a2f7eb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Adaman.Name",
    display_name="Adaman",
    searchable_by=["Adaman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    effect=adaman,
    condition=has_two_metal_energy_in_hand
)
