from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="08202675-968e-51ca-a73b-ed173c4f300d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brock.Name",
    display_name="Brock",
    searchable_by=["Brock"],
    subtypes=[],
    collector_number=98,
    set_code="GYM1",
    rarity=Rarities.Rare,
    condition=requires_damaged_pokemon(),
    effect=heal_item(10, scope="each_own"),
)
