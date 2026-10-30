from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import item_finder, item_finder_condition

card = ItemCardDef(
    guid="cdb60c14-3d35-5e77-b80e-0a88e9703f14",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ItemFinder.Name",
    display_name="Item Finder",
    searchable_by=["Item Finder"],
    subtypes=[],
    collector_number=103,
    set_code="BASE4",
    rarity=Rarities.Rare,
    condition=item_finder_condition,
    effect=item_finder,
)
