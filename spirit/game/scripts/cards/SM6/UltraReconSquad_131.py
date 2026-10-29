from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import ultra_recon_squad, ultra_recon_squad_condition

card = SupporterCardDef(
    guid="c09dd4bc-6c3f-50c1-ac9b-32d90a284c16",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraReconSquad.Name",
    display_name="Ultra Recon Squad",
    searchable_by=["Ultra Recon Squad", "Supporter"],
    subtypes=["Supporter"],
    collector_number=131,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    condition=ultra_recon_squad_condition,
    effect=ultra_recon_squad,
)
