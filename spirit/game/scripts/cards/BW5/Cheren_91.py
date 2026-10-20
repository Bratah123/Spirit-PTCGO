from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="338bd264-b101-5b7b-8999-bf832ea6fd09",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cheren.Name",
    display_name="Cheren",
    searchable_by=["Cheren", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3)
)
