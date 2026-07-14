from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import scoop_up_net

card = ItemCardDef(
    guid="3046823f-6e39-5c6a-a447-692894877a01",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUpNet.Name",
    display_name="Scoop Up Net",
    searchable_by=["Scoop Up Net", "Item"],
    subtypes=["Item"],
    collector_number=207,
    set_code="SWSH2",
    rarity=Rarities.RareSecret,
    effect=scoop_up_net
)
