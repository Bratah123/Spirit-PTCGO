from spirit.game.card_effects.trainers import fan_of_waves, opponent_has_special_energy
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8ce5a607-70d8-5715-b3d5-4b948b6e9454",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FanofWaves.Name",
    display_name="Fan of Waves",
    searchable_by=["Fan of Waves", "Item", "Rapid Strike"],
    subtypes=["Item", "Rapid Strike"],
    collector_number=127,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    effect=fan_of_waves,
    condition=opponent_has_special_energy
)
