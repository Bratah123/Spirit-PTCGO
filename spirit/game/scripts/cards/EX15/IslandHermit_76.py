"""EX15 Dragon Frontiers — Island Hermit."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import island_hermit_prizes_face_up

card = SupporterCardDef(
    guid="2e00cf9d-cae1-542c-9f08-2b45cd8ea345",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandHermit.Name",
    display_name="Island Hermit",
    searchable_by=["Island Hermit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=76,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=island_hermit_prizes_face_up(2, 2),
)
