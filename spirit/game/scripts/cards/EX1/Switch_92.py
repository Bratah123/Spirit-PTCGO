from spirit.game.card_effects.trainers import switch, player_has_bench, play_targets
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="09f19685-9fc7-5223-9db5-909a6fb89907",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="EX1",
    rarity=Rarities.Common,
    effect=switch,
    play_targets=play_targets(opponent=False, bench_only=True),
    play_target_prompt="",
    condition=player_has_bench
)

