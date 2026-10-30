"""EX12 Legend Maker — Fieldworker supporter.
"""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import fieldworker_draw


card = SupporterCardDef(
    guid="1b5a5348-83e6-52c5-ac7a-e31ba5e339a1",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fieldworker.Name",
    display_name="Fieldworker",
    searchable_by=["Fieldworker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    effect=fieldworker_draw(),
)
