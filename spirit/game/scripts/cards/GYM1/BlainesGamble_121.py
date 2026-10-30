from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaines_gamble


card = ItemCardDef(
    guid="6323b3d5-1cea-545a-bf23-cd0b376a5082",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesGamble.Name",
    display_name="Blaine's Gamble",
    searchable_by=["Blaine's Gamble"],
    subtypes=[],
    collector_number=121,
    set_code="GYM1",
    rarity=Rarities.Common,
    effect=blaines_gamble,
)
