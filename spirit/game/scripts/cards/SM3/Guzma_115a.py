from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import guzma, guzma_condition

card = SupporterCardDef(
    guid="7e572dfe-c58b-53b0-86bb-85b34e9b275b",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=guzma_condition,
    effect=guzma,)
