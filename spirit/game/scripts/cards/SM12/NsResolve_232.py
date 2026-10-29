from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import ns_resolve

card = SupporterCardDef(
    guid="5c7b155b-6b99-5809-9447-cf7caf499803",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsResolve.Name",
    display_name="N's Resolve",
    searchable_by=["N's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=232,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=ns_resolve,
)
