from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import plus_power, plus_power_passive


card = ItemCardDef(
    guid="2a170ab2-372d-5662-a59d-51aa5e446bd5",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower"],
    subtypes=[],
    collector_number=113,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=plus_power,
)
card.passive = plus_power_passive
