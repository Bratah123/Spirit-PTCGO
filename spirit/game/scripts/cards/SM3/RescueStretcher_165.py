from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.SM2.RescueStretcher_130 import (
    rescue_stretcher, rescue_stretcher_playable,
)

card = ItemCardDef(
    guid="653e090e-d8be-5477-b622-30f83c5e6d06",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    condition=rescue_stretcher_playable,
    effect=rescue_stretcher,
)
