from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import blues_tactics

card = SupporterCardDef(guid='9031ea95-0e83-52a4-8287-7326fbda4a04', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.BluesTactics.Name', display_name="Blue's Tactics", searchable_by=["Blue's Tactics", 'Supporter'], subtypes=['Supporter'], collector_number=188, set_code='SM11', rarity=Rarities.Uncommon, effect=blues_tactics)
