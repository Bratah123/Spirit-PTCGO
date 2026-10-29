from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import MT_CORONET_ABILITY

card = StadiumCardDef(
    guid="a5e0c70a-ae34-542b-bbab-8a774b4b9348",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium"],
    subtypes=["Stadium"],
    collector_number=130,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    ability=MT_CORONET_ABILITY,
)
