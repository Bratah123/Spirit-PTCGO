from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import is_unown
from spirit.game.card_effects.support_common import requires_bench_space, search_to_bench


card = ItemCardDef(
    guid="a0881ca1-94ef-5432-a287-d0ba20123a69",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RuinWall.Name",
    display_name="Ruin Wall",
    searchable_by=["Ruin Wall"],
    subtypes=[],
    collector_number=74,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    condition=requires_bench_space(1),
    effect=search_to_bench(
        is_unown,
        prompt="Choose a card with Unown in its name to put onto your Bench.",
    ),
)
