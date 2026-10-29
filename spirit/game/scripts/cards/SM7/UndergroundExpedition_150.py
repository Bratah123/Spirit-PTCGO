from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    underground_expedition,
    underground_expedition_condition,
)

card = SupporterCardDef(
    guid="8e14809a-ab53-554a-8897-7c48c6b2b730",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=underground_expedition,
    condition=underground_expedition_condition,
)
