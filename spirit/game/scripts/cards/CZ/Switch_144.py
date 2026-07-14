from spirit.game.card_effects.trainers import player_has_bench, switch
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7f3a03ee-026f-504e-b07d-28dc8f57f2cf",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=144,
    set_code="CZ",
    rarity=Rarities.Common,
    effect=switch,
    condition=player_has_bench
)
