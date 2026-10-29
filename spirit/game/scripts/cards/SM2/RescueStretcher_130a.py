from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.SM2.RescueStretcher_130 import (
    rescue_stretcher, rescue_stretcher_playable,
)

card = ItemCardDef(
    guid="223ea9a6-01e8-5520-9ed8-ba868ef81245",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=179,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=rescue_stretcher_playable,
    effect=rescue_stretcher,
)
