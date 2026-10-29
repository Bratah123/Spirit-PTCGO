from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_special_energy
from spirit.game.scripts.cards.SM2.EnhancedHammer_124 import enhanced_hammer

card = ItemCardDef(
    guid="170fe1d6-bba9-5ee6-93d8-f20687db8f5c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=162,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    condition=opponent_has_special_energy,
    effect=enhanced_hammer,
)
