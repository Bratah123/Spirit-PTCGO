from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import tormenting_spray, tormenting_spray_playable

card = ItemCardDef(
    guid="6957d25d-fda7-5fb4-8096-e34502d64d7d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TormentingSpray.Name",
    display_name="Tormenting Spray",
    searchable_by=["Tormenting Spray", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    condition=tormenting_spray_playable,
    effect=tormenting_spray,)
