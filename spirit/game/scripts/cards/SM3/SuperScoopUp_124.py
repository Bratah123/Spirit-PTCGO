from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import super_scoop_up

card = ItemCardDef(
    guid="d9469aa4-6859-537a-9dae-50ca13a6f394",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,)
