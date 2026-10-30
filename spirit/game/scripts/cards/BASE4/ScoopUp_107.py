from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import scoop_up


card = ItemCardDef(
    guid="f7a97997-9557-5ac0-8e72-cfa42680a4ab",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUp.Name",
    display_name="Scoop Up",
    searchable_by=["Scoop Up"],
    subtypes=[],
    collector_number=107,
    set_code="BASE4",
    rarity=Rarities.Rare,
    effect=scoop_up,
)
