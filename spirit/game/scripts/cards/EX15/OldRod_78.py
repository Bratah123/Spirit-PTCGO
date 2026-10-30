"""EX15 Dragon Frontiers — Old Rod."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import old_rod_flip2

card = ItemCardDef(
    guid="31ad4660-f40b-5c53-bace-f47b33c8155c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldRod.Name",
    display_name="Old Rod",
    searchable_by=["Old Rod", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=old_rod_flip2(),
)
