from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import scoop_up_net

card = ItemCardDef(
    guid="d7034d20-559f-5ccd-951d-3af7674f2a4a",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUpNet.Name",
    display_name="Scoop Up Net",
    searchable_by=["Scoop Up Net", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=scoop_up_net,
)
