from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import celios_network

card = SupporterCardDef(
    guid="87595c4e-2fd3-5b46-a9ea-9229a1829f23",
    key="TK2B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=8,
    set_code="TK2B",
    rarity=Rarities.Common,
    effect=celios_network,
)
