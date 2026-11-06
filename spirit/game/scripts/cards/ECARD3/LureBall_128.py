from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import lure_ball


card = ItemCardDef(
    guid="485fd11c-7e32-5770-a251-d19e8c24ae30",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureBall.Name",
    display_name="Lure Ball",
    searchable_by=["Lure Ball"],
    subtypes=[],
    collector_number=128,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=lure_ball,
)
