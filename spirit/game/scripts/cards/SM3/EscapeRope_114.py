from spirit.game.card_effects.trainers import escape_rope, someone_has_bench
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5f83a367-f2c4-5268-849f-0977d133146c",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeRope.Name",
    display_name="Escape Rope",
    searchable_by=["Escape Rope", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=escape_rope,
    condition=someone_has_bench
)
