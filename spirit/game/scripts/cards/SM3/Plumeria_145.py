from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import plumeria, plumeria_playable

card = SupporterCardDef(
    guid="16bc444e-26f7-5fbc-b21d-7655d5b2aba7",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name",
    display_name="Plumeria",
    searchable_by=["Plumeria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    condition=plumeria_playable,
    effect=plumeria,)
