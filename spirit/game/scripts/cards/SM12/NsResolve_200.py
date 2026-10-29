from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import ns_resolve

card = SupporterCardDef(
    guid="274dde60-f147-5ff6-8a63-ebc1e5b0f749",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NsResolve.Name",
    display_name="N's Resolve",
    searchable_by=["N's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=ns_resolve,
)
