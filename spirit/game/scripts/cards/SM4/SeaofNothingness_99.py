from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import SeaOfNothingnessPassive

card = StadiumCardDef(
    guid="04a257d7-809b-512d-abb0-4e7d40f3d244",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SeaofNothingness.Name",
    display_name="Sea of Nothingness",
    searchable_by=["Sea of Nothingness", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=SeaOfNothingnessPassive(),
)
