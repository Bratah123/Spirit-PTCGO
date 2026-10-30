"""Premier Ball (DP4 #101)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import premier_ball

card = ItemCardDef(
    guid="5db00b25-470e-5f43-a62b-0d2ee554e6ec",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremierBall.Name",
    display_name="Premier Ball",
    searchable_by=["Premier Ball", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    effect=premier_ball(),
)
