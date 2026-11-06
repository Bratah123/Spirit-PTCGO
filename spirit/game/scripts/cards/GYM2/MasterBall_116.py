from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck, master_ball


card = ItemCardDef(
    guid="3174f8da-44dc-58e3-9d1b-eca9871f4154",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball"],
    subtypes=[],
    collector_number=116,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=master_ball,
)
