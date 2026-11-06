from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import blaines_last_resort, only_card_in_hand


card = ItemCardDef(
    guid="bee093f9-1659-5487-bddb-424a66bb09cd",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastResort.Name",
    display_name="Blaine's Last Resort",
    searchable_by=["Blaine's Last Resort"],
    subtypes=[],
    collector_number=105,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=only_card_in_hand,
    effect=blaines_last_resort,
)
