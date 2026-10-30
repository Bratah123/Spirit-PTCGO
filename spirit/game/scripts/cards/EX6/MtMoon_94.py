from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import mt_moon_passive

card = StadiumCardDef(
    guid="71fb1a9d-63cb-5cee-af3c-cc7c8202a493",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtMoon.Name",
    display_name="Mt. Moon",
    searchable_by=["Mt. Moon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    passive=mt_moon_passive(),
)
