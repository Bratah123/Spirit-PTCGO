"""EX16 Power Keepers — Drake's Stadium."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import drakes_stadium_passive

card = StadiumCardDef(
    guid="4e066e60-33ce-58e7-9b45-653258aef9ce",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DrakesStadium.Name",
    display_name="Drake's Stadium",
    searchable_by=["Drake's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=72,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=drakes_stadium_passive(),
)
