from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import tag_call

card = ItemCardDef(
    guid="034de107-16f2-542a-93bc-ad786eb1b7b4",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagCall.Name",
    display_name="Tag Call",
    searchable_by=["Tag Call", "Item"],
    subtypes=["Item"],
    collector_number=270,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=tag_call,
)
