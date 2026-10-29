from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import acerola, acerola_condition

card = SupporterCardDef(
    guid="14a0b888-bb49-5ec2-82c4-42948c835eb5",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=acerola_condition,
    effect=acerola,)
