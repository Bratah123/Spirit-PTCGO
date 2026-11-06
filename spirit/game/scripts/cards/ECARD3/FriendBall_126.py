from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import friend_ball


card = ItemCardDef(
    guid="75f614bb-d080-5e24-bfad-ee98ee865d09",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendBall.Name",
    display_name="Friend Ball",
    searchable_by=["Friend Ball"],
    subtypes=[],
    collector_number=126,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=friend_ball,
)
