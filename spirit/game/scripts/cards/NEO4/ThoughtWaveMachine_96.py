from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import thought_wave_machine


card = ItemCardDef(
    guid="98ec0812-e124-51e7-ad24-93e77612bb91",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThoughtWaveMachine.Name",
    display_name="Thought Wave Machine",
    searchable_by=["Thought Wave Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=96,
    set_code="NEO4",
    rarity=Rarities.Rare,
    effect=thought_wave_machine,
)
