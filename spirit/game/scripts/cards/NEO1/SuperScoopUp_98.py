from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import super_scoop_up


card = ItemCardDef(
    guid="48e9afb5-a38e-5879-a319-3a0023a79142",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up"],
    subtypes=[],
    collector_number=98,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    effect=super_scoop_up,
)
