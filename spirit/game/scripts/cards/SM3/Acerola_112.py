from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import acerola, acerola_condition

card = SupporterCardDef(
    guid="479eac05-4692-569c-aaff-d8f88dcf0b33",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=acerola_condition,
    effect=acerola,)
