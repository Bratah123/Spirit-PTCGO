from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import magnetic_storm_passive

card = StadiumCardDef(
    guid="559444fd-2fd8-5ce1-ad6a-0c3eaeb7cb01",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagneticStorm.Name",
    display_name="Magnetic Storm",
    searchable_by=["Magnetic Storm", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    passive=magnetic_storm_passive(),
)
