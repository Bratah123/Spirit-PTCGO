from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import draw_attack

card = SupporterCardDef(
    guid="390b6e9e-9060-5a60-8e26-45816a4c3f7b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cheren.Name",
    display_name="Cheren",
    searchable_by=["Cheren", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=draw_attack(3)
)
