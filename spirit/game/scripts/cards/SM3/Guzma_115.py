from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import guzma, guzma_condition

card = SupporterCardDef(
    guid="8f333679-c841-521d-bafc-83f4529c1f97",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Guzma.Name",
    display_name="Guzma",
    searchable_by=["Guzma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=guzma_condition,
    effect=guzma,)
