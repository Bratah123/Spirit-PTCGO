from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import cyrus, cyrus_condition

card = SupporterCardDef(
    guid="4e7ff502-56ef-5e9c-aaaf-42e068e827a4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CyrusPrismStar.Name",
    display_name="Cyrus {*}",
    searchable_by=["Cyrus {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=120,
    set_code="SM5",
    rarity=Rarities.Prism,
    condition=cyrus_condition,
    effect=cyrus,
)
