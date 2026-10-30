from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.SM2.Hala_126 import hala

card = SupporterCardDef(
    guid="f3084b97-94c7-581c-8d61-9cf6f4fca24a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hala.Name",
    display_name="Hala",
    searchable_by=["Hala", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    effect=hala,
)
