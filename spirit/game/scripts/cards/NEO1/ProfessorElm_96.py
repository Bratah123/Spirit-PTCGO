from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import professor_elm


card = ItemCardDef(
    guid="270bdfe3-71b0-5f30-b9eb-90f6792edff9",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElm.Name",
    display_name="Professor Elm",
    searchable_by=["Professor Elm"],
    subtypes=[],
    collector_number=96,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    effect=professor_elm
)
