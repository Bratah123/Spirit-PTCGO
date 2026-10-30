"""DualBall_72 wired."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import dual_ball

card = ItemCardDef(
    guid="3daf1ffd-2d47-5a87-9334-14e8fbe79097",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=72,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=dual_ball()
)
