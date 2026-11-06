from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import restore_fossil


card = ItemCardDef(
    guid="a059c8ec-e1c3-549a-9aec-dd171b482c80",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlumeFossil.Name",
    display_name="Plume Fossil",
    searchable_by=["Plume Fossil", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    effect=restore_fossil("Archen"),
)
