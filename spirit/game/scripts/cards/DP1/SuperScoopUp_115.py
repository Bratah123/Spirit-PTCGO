from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import super_scoop_up

card = ItemCardDef(
    guid="70dc0081-0f41-557c-bc63-9fb42bce4a64",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,
)
