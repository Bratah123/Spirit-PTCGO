from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import mr_fuji
from spirit.game.card_effects.trainers import player_has_bench, play_targets


card = ItemCardDef(
    guid="adf5c669-018e-5a78-82f9-21f3013e9322",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrFuji.Name",
    display_name="Mr. Fuji",
    searchable_by=["Mr. Fuji"],
    subtypes=[],
    collector_number=58,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    effect=mr_fuji,
    play_targets=play_targets(opponent=False, bench_only=True),
    play_target_prompt="",
    condition=player_has_bench,
)
