from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import seer


card = SupporterCardDef(
    guid="024715b9-f516-53ea-a1f1-42e05ad073af",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Seer.Name",
    display_name="Seer",
    searchable_by=["Seer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=seer,
)
