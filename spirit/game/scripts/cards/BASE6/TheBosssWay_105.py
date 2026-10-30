from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import the_bosss_way


card = ItemCardDef(
    guid="7edfb317-233e-5d9e-8d12-b4377eef480b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheBosssWay.Name",
    display_name="The Boss's Way",
    searchable_by=["The Boss's Way"],
    subtypes=[],
    collector_number=105,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    effect=the_bosss_way,
)
