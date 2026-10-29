from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    acro_bike,
)
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="f82a585f-6923-591c-91e6-f3bcb85e341e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=acro_bike,
    condition=deck_nonempty,
)
