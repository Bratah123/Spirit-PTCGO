from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import secret_mission


card = ItemCardDef(
    guid="2052ce18-9aff-51a7-aeb8-a36dd65d6d56",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SecretMission.Name",
    display_name="Secret Mission",
    searchable_by=["Secret Mission"],
    subtypes=[],
    collector_number=118,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=secret_mission,
)
