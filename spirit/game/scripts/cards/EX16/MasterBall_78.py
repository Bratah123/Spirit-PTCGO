from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import master_ball_ex8
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="8e415aef-79fb-516d-870c-5bc63747c59a",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    effect=master_ball_ex8,
    condition=deck_nonempty,
)
