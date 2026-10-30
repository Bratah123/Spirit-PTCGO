"""EX16 Power Keepers — Phoebe's Stadium."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import phoebes_stadium_passive

card = StadiumCardDef(
    guid="cda6e567-c123-5ab4-a437-0e2dae327ca7",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PhoebesStadium.Name",
    display_name="Phoebe's Stadium",
    searchable_by=["Phoebe's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=phoebes_stadium_passive(),
)
