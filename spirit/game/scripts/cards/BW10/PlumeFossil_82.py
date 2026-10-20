from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import restore_fossil

card = ItemCardDef(
    guid="9fcd7409-97fd-52b2-bb48-d2f70c8bbfbc",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlumeFossil.Name",
    display_name="Plume Fossil",
    searchable_by=["Plume Fossil", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=restore_fossil("Archen")
)
