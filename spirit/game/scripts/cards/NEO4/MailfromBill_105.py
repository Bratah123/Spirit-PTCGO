from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import mail_from_bill_condition
from spirit.game.card_effects.support_common import draw_until_effect


card = ItemCardDef(
    guid="27303010-e742-528f-b79a-fd21900a16c2",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MailfromBill.Name",
    display_name="Mail from Bill",
    searchable_by=["Mail from Bill"],
    subtypes=[],
    collector_number=105,
    set_code="NEO4",
    rarity=Rarities.Common,
    condition=mail_from_bill_condition,
    effect=draw_until_effect(4),
)
