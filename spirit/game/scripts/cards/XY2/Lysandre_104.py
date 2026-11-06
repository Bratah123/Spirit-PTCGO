from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench, opponent_play_targets

card = SupporterCardDef(
    guid="6e2ee7b2-2b80-5617-ab6f-e8de5d58a8a9",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="XY2",
    rarity=Rarities.RareUltra,
    effect=bosss_orders,
    play_targets=opponent_play_targets(bench_only=True),
    play_target_prompt="Choose the opponent's new Active Pokémon",
    condition=opponent_has_bench
)
