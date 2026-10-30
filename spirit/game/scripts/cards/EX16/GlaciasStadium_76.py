"""EX16 Power Keepers — Glacia's Stadium."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import glacias_stadium_passive

card = StadiumCardDef(
    guid="4b488e3f-e650-59ad-9c65-a215393f3d1d",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlaciasStadium.Name",
    display_name="Glacia's Stadium",
    searchable_by=["Glacia's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=glacias_stadium_passive(),
)
