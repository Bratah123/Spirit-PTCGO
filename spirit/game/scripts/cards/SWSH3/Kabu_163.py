from spirit.game.card_effects.trainers import kabu
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f5b336b1-53bd-558f-a7b7-f17cfb8d2f63",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kabu.Name",
    display_name="Kabu",
    searchable_by=["Kabu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=kabu
)
