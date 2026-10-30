from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import super_scoop_up

card = ItemCardDef(
    guid="48433d75-29c2-57e7-b2dd-028d8e9c8731",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,
)
