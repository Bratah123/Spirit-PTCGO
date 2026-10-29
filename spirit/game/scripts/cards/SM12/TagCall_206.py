from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import tag_call

card = ItemCardDef(
    guid="04a9f03e-8f5c-5b8d-a5a2-661a1dc0ed92",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagCall.Name",
    display_name="Tag Call",
    searchable_by=["Tag Call", "Item"],
    subtypes=["Item"],
    collector_number=206,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=tag_call,
)
