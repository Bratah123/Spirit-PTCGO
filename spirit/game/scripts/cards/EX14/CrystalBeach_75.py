from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import crystal_beach_passive

card = StadiumCardDef(
    guid="c0f1f75e-b36f-5dfa-ba42-791f4f99283e",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalBeach.Name",
    display_name="Crystal Beach",
    searchable_by=["Crystal Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=75,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=crystal_beach_passive(),
)
