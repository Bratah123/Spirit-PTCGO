from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import ancient_tomb_passive

card = StadiumCardDef(
    guid="c9f6d6ad-d4c9-59d8-b8fc-b8effe6caa69",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTomb.Name",
    display_name="Ancient Tomb",
    searchable_by=["Ancient Tomb", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    passive=ancient_tomb_passive(),
)
