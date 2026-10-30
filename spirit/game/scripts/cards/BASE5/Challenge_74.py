from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import challenge


card = ItemCardDef(
    guid="2060a7ff-2386-56b3-ab9f-416fdac1b1a9",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Challenge.Name",
    display_name="Challenge!",
    searchable_by=["Challenge!"],
    subtypes=[],
    collector_number=74,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    effect=challenge,
)
