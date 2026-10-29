from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import DevouredFieldPassive

card = StadiumCardDef(
    guid="e0b9123a-cf4c-5030-a17e-c52760d66796",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevouredField.Name",
    display_name="Devoured Field",
    searchable_by=["Devoured Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=DevouredFieldPassive(),
)
