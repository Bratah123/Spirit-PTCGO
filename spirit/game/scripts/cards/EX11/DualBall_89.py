"""DualBall_72 wired."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import dual_ball

card = ItemCardDef(
    guid="ad50f0d1-553e-5a3b-a9b5-b01d8759ac8f",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=dual_ball()
)
