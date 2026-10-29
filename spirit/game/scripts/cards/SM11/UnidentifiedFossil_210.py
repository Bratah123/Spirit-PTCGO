from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import FossilBodyPassive, fossil_discard_ability

card = FossilItemCardDef(guid='f97daa3b-d8bf-5380-b4e9-4ccfdd9c6cd1', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.UnidentifiedFossil.Name', display_name='Unidentified Fossil', searchable_by=['Unidentified Fossil', 'Item'], subtypes=['Item'], collector_number=210, set_code='SM11', rarity=Rarities.Uncommon, hp=60, passive=FossilBodyPassive(), abilities=[fossil_discard_ability()])
