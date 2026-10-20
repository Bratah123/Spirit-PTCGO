from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4d483d2e-a05e-5b87-8990-c34c62119e1c",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=100,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
