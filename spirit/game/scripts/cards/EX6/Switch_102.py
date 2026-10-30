from spirit.game.card_effects.trainers import switch, player_has_bench, play_targets
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="074a1710-3ef7-5c27-96d6-f07eb3200fae",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="EX6",
    rarity=Rarities.Common,
    effect=switch,
    play_targets=play_targets(opponent=False, bench_only=True),
    play_target_prompt="",
    condition=player_has_bench
)

