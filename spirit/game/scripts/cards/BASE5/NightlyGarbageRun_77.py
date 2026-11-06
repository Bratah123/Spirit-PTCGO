from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    nightly_garbage_run,
    nightly_garbage_run_condition,
)


card = ItemCardDef(
    guid="ed148e61-382d-587f-aeca-e7ff9a5bdda0",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightlyGarbageRun.Name",
    display_name="Nightly Garbage Run",
    searchable_by=["Nightly Garbage Run", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=77,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    condition=nightly_garbage_run_condition,
    effect=nightly_garbage_run,
)
