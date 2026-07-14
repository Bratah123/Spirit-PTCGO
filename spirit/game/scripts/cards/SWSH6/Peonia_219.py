from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import peonia, peonia_playable

card = SupporterCardDef(
    guid="cbc997d3-3608-55f8-9cc0-e0517d7470d4",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Peonia.Name",
    display_name="Peonia",
    searchable_by=["Peonia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=219,
    set_code="SWSH6",
    rarity=Rarities.RareRainbow,
    condition=peonia_playable,
    effect=peonia,
)
