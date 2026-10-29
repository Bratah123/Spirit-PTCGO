from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import mistys_favor

card = SupporterCardDef(guid='10f4d65a-b3c7-57ce-88f6-31ad0bc0f4d9', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.MistysFavor.Name', display_name="Misty's Favor", searchable_by=["Misty's Favor", 'Supporter'], subtypes=['Supporter'], collector_number=202, set_code='SM11', rarity=Rarities.Uncommon, effect=mistys_favor)
