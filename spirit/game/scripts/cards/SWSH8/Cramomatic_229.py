from spirit.game.card_effects.trainers import cramomatic, has_other_item_in_hand
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1b2375b2-5e45-5345-812f-3938eecf4b48",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cramomatic.Name",
    display_name="Cram-o-matic",
    searchable_by=["Cram-o-matic", "Item"],
    subtypes=["Item"],
    collector_number=229,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=cramomatic,
    condition=has_other_item_in_hand
)
