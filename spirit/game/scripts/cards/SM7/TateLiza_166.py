from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    tate_liza,
    tate_liza_condition,
)

card = SupporterCardDef(
    guid="31fad7d0-76ee-5722-9734-f5dededecf30",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name",
    display_name="Tate & Liza",
    searchable_by=["Tate & Liza", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    effect=tate_liza,
    condition=tate_liza_condition,
)
