from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm6 import ultra_recon_squad, ultra_recon_squad_condition

card = SupporterCardDef(
    guid="4e341391-03da-5511-be85-f4b6f4381eb5",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraReconSquad.Name",
    display_name="Ultra Recon Squad",
    searchable_by=["Ultra Recon Squad", "Supporter"],
    subtypes=["Supporter"],
    collector_number=114,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    condition=ultra_recon_squad_condition,
    effect=ultra_recon_squad,
)
