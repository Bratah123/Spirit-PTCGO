from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item, requires_damaged_pokemon

card = ItemCardDef(
    guid="af9cff4b-a4ad-533d-8618-170449b8f35e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brock.Name",
    display_name="Brock",
    searchable_by=["Brock"],
    subtypes=[],
    collector_number=15,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    condition=requires_damaged_pokemon(),
    effect=heal_item(10, scope="each_own"),
)
