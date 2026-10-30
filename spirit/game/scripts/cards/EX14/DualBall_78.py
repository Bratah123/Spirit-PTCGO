"""DualBall_72 wired."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import dual_ball

card = ItemCardDef(
    guid="acabb243-f3f0-555a-adfa-68dda60907c8",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=dual_ball()
)
