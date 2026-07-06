from spirit.game.card_effects.trainers import milo
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="512f897d-f46b-5a76-bd69-271664534030",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Milo.Name",
    display_name="Milo",
    searchable_by=["Milo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=milo
)
