from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import revive, revive_condition


card = ItemCardDef(
    guid="b45cab76-43ab-53db-87d5-790f3ac63c9a",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive"],
    subtypes=[],
    collector_number=89,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    condition=revive_condition,
    effect=revive,
)
