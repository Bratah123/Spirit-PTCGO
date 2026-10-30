from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import super_scoop_up

card = ItemCardDef(
    guid="841eb7e9-b705-5ba1-a513-5f592b470660",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,
)
