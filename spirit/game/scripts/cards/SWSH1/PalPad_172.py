from spirit.game.card_effects.trainers import has_supporter_in_discard, pal_pad
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="edcaf9fc-50a2-53aa-9069-47a1d04edac2",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PalPad.Name",
    display_name="Pal Pad",
    searchable_by=["Pal Pad", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=pal_pad,
    condition=has_supporter_in_discard
)
