from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6a490558-dc70-5aa3-80ea-a2f3747a9725",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name",
    display_name="Pok\u00e9dex",
    searchable_by=["Pokédex", "Item"],
    subtypes=["Item"],
    collector_number=98,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
