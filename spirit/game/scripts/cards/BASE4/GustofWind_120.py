from spirit.game.card_effects.trainers import (
    bosss_orders, opponent_has_bench, opponent_play_targets,
)
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


card = ItemCardDef(
    guid="beed2548-4563-5060-8181-6326bcd7aea0",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GustofWind.Name",
    display_name="Gust of Wind",
    searchable_by=["Gust of Wind"],
    subtypes=[],
    collector_number=120,
    set_code="BASE4",
    rarity=Rarities.Common,
    effect=bosss_orders,
    play_targets=opponent_play_targets(bench_only=True),
    play_target_prompt="Choose the opponent's new Active Pokémon",
    condition=opponent_has_bench,
)
