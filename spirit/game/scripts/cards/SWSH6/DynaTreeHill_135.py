from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import healing_block_passive

card = StadiumCardDef(
    guid="af0a7546-b634-5b1c-a755-85676a0a267c",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DynaTreeHill.Name",
    display_name="Dyna Tree Hill",
    searchable_by=["Dyna Tree Hill", "Stadium"],
    subtypes=["Stadium"],
    collector_number=135,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    passive=healing_block_passive(lambda target, carrier: True),
)
