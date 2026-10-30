from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import swoop_teleporter

card = ItemCardDef(
    guid="950e6cc8-d11f-5e1c-9b36-3a9a78d831ce",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwoopTeleporter.Name",
    display_name="Swoop! Teleporter",
    searchable_by=["Swoop! Teleporter", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=92,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    effect=swoop_teleporter,
)
