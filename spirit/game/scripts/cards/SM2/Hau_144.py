from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="5a3e6ba1-fe8c-5de0-bcc6-8505eb765d3f",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    effect=draw_attack(3),
    condition=deck_nonempty
)
