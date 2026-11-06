from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import underground_expedition


card = SupporterCardDef(
    guid="ea800af8-3660-55aa-afb1-8313ccd1e58a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=underground_expedition,
)
