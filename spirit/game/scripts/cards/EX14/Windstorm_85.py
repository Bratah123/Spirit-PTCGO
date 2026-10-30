from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import windstorm_discard_tools_stadiums

card = ItemCardDef(
    guid="db3d3b1c-9b4b-5089-989b-7f0711b2423d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Windstorm.Name",
    display_name="Windstorm",
    searchable_by=["Windstorm", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    effect=windstorm_discard_tools_stadiums(2),
)
