from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import acerola, acerola_condition

card = SupporterCardDef(
    guid="3d86fdf6-021a-55fd-9382-77f4b147a22c",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=142,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    condition=acerola_condition,
    effect=acerola,)
