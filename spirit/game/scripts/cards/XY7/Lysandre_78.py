from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import bosss_orders, opponent_has_bench, opponent_play_targets

card = SupporterCardDef(
    guid="a1dcc4ec-3463-5c03-a295-68f0dada2c25",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre",
    searchable_by=["Lysandre", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=bosss_orders,
    play_targets=opponent_play_targets(bench_only=True),
    play_target_prompt="Choose the opponent's new Active Pokémon",
    condition=opponent_has_bench
)
