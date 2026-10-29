from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import (
    counter_catcher, counter_catcher_condition, opponent_play_targets,
)

card = ItemCardDef(
    guid="8f9c9ca5-b3b6-5388-a3c6-651ee30c3d0b",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    effect=counter_catcher,
    condition=counter_catcher_condition,
    play_targets=opponent_play_targets(bench_only=True),
)
