from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import heal_powder


card = ItemCardDef(
    guid="644d3e22-e44d-58b6-b4ea-715016f5fe23",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealPowder.Name",
    display_name="Heal Powder",
    searchable_by=["Heal Powder"],
    subtypes=[],
    collector_number=104,
    set_code="NEO4",
    rarity=Rarities.Common,
    effect=heal_powder,
)
