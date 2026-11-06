from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import energy_amplifier, energy_amplifier_condition


card = ItemCardDef(
    guid="a88e1551-714b-5896-9da4-eeecb122d0c4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyAmplifier.Name",
    display_name="Energy Amplifier",
    searchable_by=["Energy Amplifier"],
    subtypes=[],
    collector_number=98,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    condition=energy_amplifier_condition,
    effect=energy_amplifier,
)
