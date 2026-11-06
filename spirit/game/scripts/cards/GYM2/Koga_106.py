from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import koga


card = ItemCardDef(
    guid="cc32b87f-4cca-5a0c-bf60-b5e3fd4f1cf3",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Koga.Name",
    display_name="Koga",
    searchable_by=["Koga"],
    subtypes=[],
    collector_number=106,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=koga,
)
