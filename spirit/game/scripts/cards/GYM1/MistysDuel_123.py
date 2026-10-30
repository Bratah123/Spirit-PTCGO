from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import mistys_duel


card = ItemCardDef(
    guid="f619ee51-f7cb-5140-aadc-aae64672190b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDuel.Name",
    display_name="Misty's Duel",
    searchable_by=["Misty's Duel"],
    subtypes=[],
    collector_number=123,
    set_code="GYM1",
    rarity=Rarities.Common,
    effect=mistys_duel,
)
