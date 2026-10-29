from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import reset_stamp

card = ItemCardDef(guid='6c3be686-33f1-51fd-8b2f-126b0e7481a0', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name', display_name='Reset Stamp', searchable_by=['Reset Stamp', 'Item'], subtypes=['Item'], collector_number=253, set_code='SM11', rarity=Rarities.RareSecret, effect=reset_stamp)
