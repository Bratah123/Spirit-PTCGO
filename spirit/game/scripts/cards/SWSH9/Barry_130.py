from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hop

card = SupporterCardDef(
    guid="ab263a03-c4aa-50dc-833e-a8e2e65ed86c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Barry.Name",
    display_name="Barry",
    searchable_by=["Barry", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=hop
)
