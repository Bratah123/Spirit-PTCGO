from spirit.game.card_effects.trainers import switch, player_has_bench, play_targets
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3bcdc1ed-0a35-5da8-ae4e-ee26b06c5af8",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=119,
    set_code="DP1",
    rarity=Rarities.Common,
    effect=switch,
    play_targets=play_targets(opponent=False, bench_only=True),
    play_target_prompt="",
    condition=player_has_bench
)

