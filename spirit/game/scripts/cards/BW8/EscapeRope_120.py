from spirit.game.card_effects.trainers import escape_rope, someone_has_bench
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="21a60ae2-5b81-5fe1-8518-76a2b464c901",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeRope.Name",
    display_name="Escape Rope",
    searchable_by=["Escape Rope", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=escape_rope,
    condition=someone_has_bench
)
