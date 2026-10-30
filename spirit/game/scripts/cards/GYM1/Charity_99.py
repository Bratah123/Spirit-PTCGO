from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import charity, charity_passive


card = ItemCardDef(
    guid="b0898764-db83-5141-afef-f86d276185f7",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Charity.Name",
    display_name="Charity",
    searchable_by=["Charity"],
    subtypes=[],
    collector_number=99,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=charity,
)
card.passive = charity_passive
