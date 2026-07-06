from spirit.game.card_effects.trainers import kamado, hand_size_at_least
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7d902cde-2a56-509c-8322-211f0f42fa2f",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kamado.Name",
    display_name="Kamado",
    searchable_by=["Kamado", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=kamado,
    condition=hand_size_at_least(2)
)
