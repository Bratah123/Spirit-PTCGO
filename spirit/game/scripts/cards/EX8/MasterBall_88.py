from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import master_ball_ex8
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="05ad62a2-580f-5aa8-ab96-b43e5a3a6a66",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=master_ball_ex8,
    condition=deck_nonempty,
)
