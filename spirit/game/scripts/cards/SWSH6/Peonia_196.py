from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import peonia, peonia_playable

card = SupporterCardDef(
    guid="174156d7-f142-57b2-980a-90f2f9b91aac",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Peonia.Name",
    display_name="Peonia",
    searchable_by=["Peonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=196,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    condition=peonia_playable,
    effect=peonia,
)
