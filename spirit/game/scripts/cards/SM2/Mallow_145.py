from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty
from spirit.game.scripts.cards.SM2.Mallow_127 import mallow

card = SupporterCardDef(
    guid="8950d6b8-765a-59c0-91b7-e44b5cc149b3",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mallow.Name",
    display_name="Mallow",
    searchable_by=["Mallow", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    condition=deck_nonempty,
    effect=mallow,
)
