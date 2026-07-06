from spirit.game.card_effects.trainers import fan_of_waves, opponent_has_special_energy
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4a853e86-ca91-5884-952e-1882bd52966b",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FanofWaves.Name",
    display_name="Fan of Waves",
    searchable_by=["Fan of Waves", "Item", "Rapid Strike"],
    subtypes=["Item", "Rapid Strike"],
    collector_number=226,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    effect=fan_of_waves,
    condition=opponent_has_special_energy
)
