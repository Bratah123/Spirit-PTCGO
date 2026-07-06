from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f89061d7-f95e-5324-973e-a2b65b98ece2",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=147,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    effect=professors_research
)
