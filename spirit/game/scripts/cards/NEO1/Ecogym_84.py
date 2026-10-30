from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import ecogym_passive


card = StadiumCardDef(
    guid="49d16f73-cbb4-58d7-ad36-fc862a7a73be",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ecogym.Name",
    display_name="Ecogym",
    searchable_by=["Ecogym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=84,
    set_code="NEO1",
    rarity=Rarities.Rare,
    passive=ecogym_passive,
)
