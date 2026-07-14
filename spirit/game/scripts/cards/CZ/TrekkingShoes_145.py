from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import trekking_shoes, deck_nonempty

card = ItemCardDef(
    guid="907ef9c5-8fe9-5606-9442-e02595c3a5ea",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrekkingShoes.Name",
    display_name="Trekking Shoes",
    searchable_by=["Trekking Shoes", "Item"],
    subtypes=["Item"],
    collector_number=145,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=trekking_shoes,
)
