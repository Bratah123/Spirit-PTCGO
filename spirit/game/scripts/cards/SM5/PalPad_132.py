from spirit.game.card_effects.trainers import has_supporter_in_discard, pal_pad
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3fc95433-f1bc-5080-b3f9-36183a475eba",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PalPad.Name",
    display_name="Pal Pad",
    searchable_by=["Pal Pad", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    effect=pal_pad,
    condition=has_supporter_in_discard
)
