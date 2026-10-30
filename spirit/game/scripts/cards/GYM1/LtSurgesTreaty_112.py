from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import lt_surges_treaty


card = ItemCardDef(
    guid="66d88f43-01aa-573a-88ae-9b7efbe4af1f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesTreaty.Name",
    display_name="Lt. Surge's Treaty",
    searchable_by=["Lt. Surge's Treaty"],
    subtypes=[],
    collector_number=112,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=lt_surges_treaty,
)
