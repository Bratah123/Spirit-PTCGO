from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import challenge


card = ItemCardDef(
    guid="c1374ece-0e52-5734-8061-b464472838ca",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Challenge.Name",
    display_name="Challenge!",
    searchable_by=["Challenge!"],
    subtypes=[],
    collector_number=106,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    effect=challenge,
)
