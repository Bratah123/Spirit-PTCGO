from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_until_effect

card = ItemCardDef(
    guid="729aa283-a8d0-54cf-b685-2ae687ca2562",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bicycle.Name",
    display_name="Bicycle",
    searchable_by=["Bicycle", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=draw_until_effect(4)
)
