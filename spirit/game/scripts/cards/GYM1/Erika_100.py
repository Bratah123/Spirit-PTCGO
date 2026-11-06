from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import erika


card = ItemCardDef(
    guid="fe02825e-4cbe-5bc4-a87c-c7b44dc67364",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika"],
    subtypes=[],
    collector_number=100,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=erika,
)
