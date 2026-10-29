from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import guzma, guzma_condition

card = SupporterCardDef(
    guid="a285a3ee-6fc7-530e-a604-4615e2129712",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=153,
    set_code="HF",
    rarity=Rarities.RareUltra,
    condition=guzma_condition,
    effect=guzma,)
