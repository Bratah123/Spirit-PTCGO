from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import lanas_fishing_rod

card = ItemCardDef(
    guid="ce1ff911-03ad-5070-9ccf-16c16af8f7a0",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasFishingRod.Name",
    display_name="Lana's Fishing Rod",
    searchable_by=["Lana's Fishing Rod", "Item"],
    subtypes=["Item"],
    collector_number=195,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=lanas_fishing_rod,
)
