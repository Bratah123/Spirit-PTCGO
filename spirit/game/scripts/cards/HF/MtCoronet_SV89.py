from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import MT_CORONET_ABILITY

card = StadiumCardDef(
    guid="7149eb36-4b7f-5cae-aef6-7507bda35ab6",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium"],
    subtypes=["Stadium"],
    collector_number=158,
    set_code="HF",
    rarity=Rarities.RareSecret,
    ability=MT_CORONET_ABILITY,
)
