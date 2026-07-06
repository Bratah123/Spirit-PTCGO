from spirit.game.card_effects.trainers import kamado, hand_size_at_least
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="508322c3-6e1c-5d9f-86f2-e1d1ee65db3b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kamado.Name",
    display_name="Kamado",
    searchable_by=["Kamado", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    effect=kamado,
    condition=hand_size_at_least(2)
)
