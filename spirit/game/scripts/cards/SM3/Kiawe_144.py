from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import kiawe

card = SupporterCardDef(
    guid="760aaaff-5595-5285-9b77-e4236bdfaf99",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=kiawe,)
