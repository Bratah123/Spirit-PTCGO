from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import fast_ball
from spirit.game.card_effects.trainers import deck_nonempty

card = ItemCardDef(
    guid="b061d93d-7948-5f3f-9d2b-9528b82c0ad1",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FastBall.Name",
    display_name="Fast Ball",
    searchable_by=["Fast Ball"],
    subtypes=[],
    collector_number=124,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    condition=deck_nonempty,
    effect=fast_ball,
)
