from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import surprise_time_machine

card = ItemCardDef(
    guid="a37144f2-53be-5d82-989d-42d73e4a4d2b",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurpriseTimeMachine.Name",
    display_name="Surprise! Time Machine",
    searchable_by=["Surprise! Time Machine", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=91,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=surprise_time_machine,
)
