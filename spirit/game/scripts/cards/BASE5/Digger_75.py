from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import digger


card = ItemCardDef(
    guid="9c522fe8-21c4-5527-bfbb-7ba6471a3be4",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Digger.Name",
    display_name="Digger",
    searchable_by=["Digger", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=75,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    effect=digger,
)
