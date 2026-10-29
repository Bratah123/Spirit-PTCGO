from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.trainers import deck_nonempty

card = SupporterCardDef(
    guid="1ab3de67-7cea-5db7-b176-8758dfae4ff7",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3),
    condition=deck_nonempty
)
