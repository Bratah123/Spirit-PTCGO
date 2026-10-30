from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import celios_network

card = SupporterCardDef(
    guid="3cafbf7c-2b94-5525-81d9-bc133819cc01",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=celios_network,
)
