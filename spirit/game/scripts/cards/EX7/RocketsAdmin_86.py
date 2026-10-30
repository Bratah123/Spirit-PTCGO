from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import rockets_admin

card = SupporterCardDef(
    guid="c3c090b0-c699-54e5-ab59-60890a9c6fd6",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsAdmin.Name",
    display_name="Rocket's Admin.",
    searchable_by=["Rocket's Admin.", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=rockets_admin,
)
