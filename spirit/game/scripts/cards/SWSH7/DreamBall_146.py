from spirit.game.data_utils import ItemCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import (
    dream_ball, dream_ball_playable, dream_ball_prize_window,
)

card = ItemCardDef(
    guid="1810e745-9155-58d2-aaea-90e36b3eeb11",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DreamBall.Name",
    display_name="Dream Ball",
    searchable_by=["Dream Ball", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    effect=dream_ball,
    condition=dream_ball_playable,
    abilities=[
        Ability(
            title="Dream Ball",
            game_text="You can play this card only if you took it as a face-down Prize card, before you put it into your hand.",
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=dream_ball_prize_window,
        ),
    ],
)
