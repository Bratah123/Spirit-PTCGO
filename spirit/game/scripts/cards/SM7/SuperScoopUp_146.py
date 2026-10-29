from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import super_scoop_up

card = ItemCardDef(
    guid="a632180d-16d5-587a-baae-e58e082150ba",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,
)
