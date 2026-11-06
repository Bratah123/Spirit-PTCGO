from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import sabrinas_gaze


card = ItemCardDef(
    guid="a3834562-2c17-5e08-a84f-ad8648b9f17b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasGaze.Name",
    display_name="Sabrina's Gaze",
    searchable_by=["Sabrina's Gaze"],
    subtypes=[],
    collector_number=125,
    set_code="GYM1",
    rarity=Rarities.Common,
    effect=sabrinas_gaze,
)
