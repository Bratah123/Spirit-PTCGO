from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    acro_bike,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="70d139a3-ae95-535c-a2fd-c822a92a7d6c",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=123,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=acro_bike,
    condition=deck_nonempty,
)
