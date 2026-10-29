from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import super_scoop_up

card = ItemCardDef(
    guid="38b6a143-0c08-5332-9763-2699e6c81e27",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    effect=super_scoop_up,)
