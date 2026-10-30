from spirit.game.card_effects.trainers import switch, player_has_bench, play_targets
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d1d0834d-a5bb-5f5c-9df3-c31a90df8f11",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="EX15",
    rarity=Rarities.Common,
    effect=switch,
    play_targets=play_targets(opponent=False, bench_only=True),
    play_target_prompt="",
    condition=player_has_bench
)

