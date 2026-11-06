from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import fisherman
from spirit.game.card_effects.trainers import has_basic_energy_in_discard

card = SupporterCardDef(
    guid="f1937dc1-34e8-52f3-8e0d-16cf1ab528a6",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    condition=has_basic_energy_in_discard,
    effect=fisherman,
)
