from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import plus_power, plus_power_passive


card = ItemCardDef(
    guid="48e34518-e255-5c0b-8a5e-88139b2db800",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower"],
    subtypes=[],
    collector_number=84,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=plus_power,
)
card.passive = plus_power_passive
