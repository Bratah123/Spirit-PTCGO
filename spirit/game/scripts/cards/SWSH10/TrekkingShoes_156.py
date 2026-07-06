from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import trekking_shoes, deck_nonempty

card = ItemCardDef(
    guid="b87f7862-be11-5c3c-9efe-373dc374f370",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrekkingShoes.Name",
    display_name="Trekking Shoes",
    searchable_by=["Trekking Shoes", "Item"],
    subtypes=["Item"],
    collector_number=156,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=trekking_shoes,
)
