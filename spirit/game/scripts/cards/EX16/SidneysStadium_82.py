"""EX16 Power Keepers — Sidney's Stadium."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import sidneys_stadium_passive

card = StadiumCardDef(
    guid="755abe03-b6d9-5bf6-b528-7d69d32a5e04",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SidneysStadium.Name",
    display_name="Sidney's Stadium",
    searchable_by=["Sidney's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=sidneys_stadium_passive(),
)
