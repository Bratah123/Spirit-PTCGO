from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import lanas_fishing_rod

card = ItemCardDef(
    guid="c45f0375-1147-5185-bbfc-fc5a9ace97f7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item"],
    subtypes=["Item"],
    collector_number=266,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    effect=lanas_fishing_rod,
)
