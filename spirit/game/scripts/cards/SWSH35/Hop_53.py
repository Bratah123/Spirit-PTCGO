from spirit.game.card_effects.trainers import hop
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8ae5ad47-0812-50ab-8099-d6fc207ebca9",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hop.Name",
    display_name="Hop",
    searchable_by=["Hop", "Supporter"],
    subtypes=["Supporter"],
    collector_number=53,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=hop
)
