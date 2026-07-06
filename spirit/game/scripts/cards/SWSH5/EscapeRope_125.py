from spirit.game.card_effects.trainers import escape_rope, someone_has_bench
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="49a44b53-3548-5b2f-ab20-68bf4bab240a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeRope.Name",
    display_name="Escape Rope",
    searchable_by=["Escape Rope", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    effect=escape_rope,
    condition=someone_has_bench
)
