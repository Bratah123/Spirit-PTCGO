from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import cherish_ball

card = ItemCardDef(guid='e4c3219c-86a4-5916-b99c-b1f96a23f8a8', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name', display_name='Cherish Ball', searchable_by=['Cherish Ball', 'Item'], subtypes=['Item'], collector_number=191, set_code='SM11', rarity=Rarities.Uncommon, effect=cherish_ball)
