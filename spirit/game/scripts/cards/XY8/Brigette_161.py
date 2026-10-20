from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.scripts.cards.XY8.Brigette_134 import brigette

card = SupporterCardDef(
    guid="a4b8533c-19cb-59b3-82f1-d18ad0243b96",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brigette.Name",
    display_name="Brigette",
    searchable_by=["Brigette", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    effect=brigette
)
