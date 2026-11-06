from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaine, blaine_condition


card = ItemCardDef(
    guid="513d0bf3-0059-5fc6-8142-85371715f7dc",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blaine.Name",
    display_name="Blaine",
    searchable_by=["Blaine"],
    subtypes=[],
    collector_number=17,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    condition=blaine_condition,
    effect=blaine,
)
