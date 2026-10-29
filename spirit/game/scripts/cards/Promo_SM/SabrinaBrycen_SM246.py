from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.smp import sabrina_brycen, sabrina_brycen_condition

card = SupporterCardDef(
    guid="54a7c071-836c-55d3-840c-e06814f569c5",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinaBrycen.Name",
    display_name="Sabrina & Brycen",
    searchable_by=["Sabrina & Brycen", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=246,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    condition=sabrina_brycen_condition,
    effect=sabrina_brycen,
)
