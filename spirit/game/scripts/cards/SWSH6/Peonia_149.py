from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import peonia, peonia_playable

card = SupporterCardDef(
    guid="fb09775c-8d51-5c86-a1a9-3548f5c2ed16",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Peonia.Name",
    display_name="Peonia",
    searchable_by=["Peonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    condition=peonia_playable,
    effect=peonia,
)
