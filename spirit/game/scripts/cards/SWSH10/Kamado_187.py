from spirit.game.card_effects.trainers import kamado, hand_size_at_least
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="433dfb5c-911a-56f2-b44a-9be1f03d0c6e",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kamado.Name",
    display_name="Kamado",
    searchable_by=["Kamado", "Supporter"],
    subtypes=["Supporter"],
    collector_number=187,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    effect=kamado,
    condition=hand_size_at_least(2)
)
