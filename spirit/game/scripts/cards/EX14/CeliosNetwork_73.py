from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import celios_network

card = SupporterCardDef(
    guid="5277953c-a018-5165-9db2-80ef198b7421",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeliosNetwork.Name",
    display_name="Celio's Network",
    searchable_by=["Celio's Network", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=celios_network,
)
