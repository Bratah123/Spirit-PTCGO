from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.card_effects.ex import holon_lass
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4b2c9f25-2b86-5a72-9d24-1db56be28bc5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLass.Name",
    display_name="Holon Lass",
    searchable_by=["Holon Lass", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=holon_lass()
)
