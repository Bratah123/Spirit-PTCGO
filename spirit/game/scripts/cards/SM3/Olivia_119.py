from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import olivia

card = SupporterCardDef(
    guid="0653276e-fc3a-57d1-990a-2fef3e5126cd",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olivia.Name",
    display_name="Olivia",
    searchable_by=["Olivia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=olivia,)
