from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import imposter_oaks_revenge
from spirit.game.card_effects.support_common import requires_hand

card = ItemCardDef(
    guid="649ff12a-4b3e-52ca-9ad6-840072930d2f",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterOaksRevenge.Name",
    display_name="Imposter Oak's Revenge",
    searchable_by=["Imposter Oak's Revenge"],
    subtypes=[],
    collector_number=76,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    effect=imposter_oaks_revenge,
    condition=requires_hand(n=1),
)
