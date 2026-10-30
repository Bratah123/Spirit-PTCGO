from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import erikas_kindness
from spirit.game.card_effects.support_common import requires_damaged_pokemon


card = ItemCardDef(
    guid="230115f3-ff70-5fa7-8020-3b524848fb72",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasKindness.Name",
    display_name="Erika's Kindness",
    searchable_by=["Erika's Kindness"],
    subtypes=[],
    collector_number=103,
    set_code="GYM2",
    rarity=Rarities.Rare,
    condition=requires_damaged_pokemon(side="any"),
    effect=erikas_kindness,
)
