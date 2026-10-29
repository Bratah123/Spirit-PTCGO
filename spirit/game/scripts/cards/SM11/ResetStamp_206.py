from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import reset_stamp

card = ItemCardDef(guid='3e8493ff-cb8a-56ea-9246-910bd2e970ad', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name', display_name='Reset Stamp', searchable_by=['Reset Stamp', 'Item'], subtypes=['Item'], collector_number=206, set_code='SM11', rarity=Rarities.Uncommon, effect=reset_stamp)
