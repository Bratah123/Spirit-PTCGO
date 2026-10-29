from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import reset_stamp

card = ItemCardDef(guid='e3994ea5-b641-5ba5-b27e-d0f035ad508e', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name', display_name='Reset Stamp', searchable_by=['Reset Stamp', 'Item'], subtypes=['Item'], collector_number=261, set_code='SM11', rarity=Rarities.Uncommon, effect=reset_stamp)
