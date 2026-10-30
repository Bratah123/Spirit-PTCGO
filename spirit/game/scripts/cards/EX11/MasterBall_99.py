from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import master_ball_ex8
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="077bf8e6-857a-5ee4-8e9c-8ecd9a5a4e89",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    effect=master_ball_ex8,
    condition=deck_nonempty,
)
