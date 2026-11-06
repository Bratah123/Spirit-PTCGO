from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import sleep


card = ItemCardDef(
    guid="c714eddf-86cb-5384-9b00-6e66f935d75d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sleep.Name",
    display_name="Sleep!",
    searchable_by=["Sleep!", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=79,
    set_code="BASE5",
    rarity=Rarities.Common,
    effect=sleep,
)
