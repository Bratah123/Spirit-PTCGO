from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import cherish_ball

card = ItemCardDef(guid='93beed6a-ad2e-5997-ad4f-d723a1e6dc51', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name', display_name='Cherish Ball', searchable_by=['Cherish Ball', 'Item'], subtypes=['Item'], collector_number=250, set_code='SM11', rarity=Rarities.RareSecret, effect=cherish_ball)
