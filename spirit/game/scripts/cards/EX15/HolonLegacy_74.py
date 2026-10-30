"""EX15 Dragon Frontiers — Holon Legacy stadium."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import holon_legacy_passive

card = StadiumCardDef(
    guid="88e3ed0a-012e-5bbb-8005-f080c9b86d5b",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLegacy.Name",
    display_name="Holon Legacy",
    searchable_by=["Holon Legacy", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    passive=holon_legacy_passive(),
)
