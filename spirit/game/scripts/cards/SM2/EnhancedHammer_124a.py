from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_has_special_energy
from spirit.game.scripts.cards.SM2.EnhancedHammer_124 import enhanced_hammer

card = ItemCardDef(
    guid="b0b7d30b-c42c-5e55-8717-5f93c027287c",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnhancedHammer.Name",
    display_name="Enhanced Hammer",
    searchable_by=["Enhanced Hammer", "Item"],
    subtypes=["Item"],
    collector_number=176,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=opponent_has_special_energy,
    effect=enhanced_hammer,
)
