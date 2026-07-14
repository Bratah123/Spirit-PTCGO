from spirit.game.card_effects.trainers import irida
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="953cc143-21c8-5736-9686-c20eda00b479",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Irida.Name",
    display_name="Irida",
    searchable_by=["Irida", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SWSH10",
    rarity=Rarities.RareHolo,
    effect=irida
)
