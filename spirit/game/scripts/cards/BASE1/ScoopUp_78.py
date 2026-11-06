from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import scoop_up


card = ItemCardDef(
    guid="a76df81d-1909-5b5c-b1ca-34866b3651c1",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUp.Name",
    display_name="Scoop Up",
    searchable_by=["Scoop Up"],
    subtypes=[],
    collector_number=78,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=scoop_up,
)
