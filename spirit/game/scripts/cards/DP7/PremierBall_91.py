"""Premier Ball (DP4 #101)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import premier_ball

card = ItemCardDef(
    guid="949300da-ddee-5966-92e3-cdc060912465",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PremierBall.Name",
    display_name="Premier Ball",
    searchable_by=["Premier Ball", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=premier_ball(),
)
