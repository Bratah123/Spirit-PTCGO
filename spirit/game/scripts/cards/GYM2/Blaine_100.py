from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaine, blaine_condition


card = ItemCardDef(
    guid="b52f1787-5bbe-5950-9039-2ce8435f6434",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blaine.Name",
    display_name="Blaine",
    searchable_by=["Blaine"],
    subtypes=[],
    collector_number=100,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=blaine_condition,
    effect=blaine,
)
