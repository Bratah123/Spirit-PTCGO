from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    underground_expedition,
    underground_expedition_condition,
)

card = SupporterCardDef(
    guid="50cfd7d5-0839-5841-b2aa-3702bb9caac1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=underground_expedition,
    condition=underground_expedition_condition,
)
