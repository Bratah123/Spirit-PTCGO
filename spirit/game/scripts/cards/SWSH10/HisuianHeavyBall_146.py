from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hisuian_heavy_ball

card = ItemCardDef(
    guid="a30572d8-2b7c-56b0-961c-9cce0b4223fb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HisuianHeavyBall.Name",
    display_name="Hisuian Heavy Ball",
    searchable_by=["Hisuian Heavy Ball", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    effect=hisuian_heavy_ball,
)
