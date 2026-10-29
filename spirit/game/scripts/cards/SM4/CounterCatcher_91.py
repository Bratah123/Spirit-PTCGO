from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import (
    counter_catcher, counter_catcher_condition, opponent_play_targets,
)

card = ItemCardDef(
    guid="ddc7dd43-0e60-5821-bf9d-f0f65e848a70",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    effect=counter_catcher,
    condition=counter_catcher_condition,
    play_targets=opponent_play_targets(bench_only=True),
)
