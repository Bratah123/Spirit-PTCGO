from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import lusamine, lusamine_condition

card = SupporterCardDef(
    guid="a7f7f22d-a109-5513-b901-2238d08d02b6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    effect=lusamine,
    condition=lusamine_condition,
)
