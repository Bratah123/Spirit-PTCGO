from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import max_revive, max_revive_condition


card = ItemCardDef(
    guid="6c06b163-7499-5f94-a0ca-80499d4f493b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive"],
    subtypes=[],
    collector_number=117,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=max_revive_condition,
    effect=max_revive,
)
