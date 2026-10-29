from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm11 import tag_switch, tag_switch_condition

card = ItemCardDef(guid='33950d93-fcd2-571b-b874-86f31f0ded2e', key='SM11', name='com.direwolfdigital.cake.data.archetypes.trainer.TagSwitch.Name', display_name='Tag Switch', searchable_by=['Tag Switch', 'Item'], subtypes=['Item'], collector_number=209, set_code='SM11', rarity=Rarities.Uncommon, effect=tag_switch, condition=tag_switch_condition)
