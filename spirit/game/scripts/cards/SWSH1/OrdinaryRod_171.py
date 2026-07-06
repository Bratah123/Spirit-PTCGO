from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import ordinary_rod, has_pokemon_or_basic_energy_in_discard

card = ItemCardDef(
    guid="0318f871-3a08-5a1a-b861-ae4aac9ca599",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OrdinaryRod.Name",
    display_name="Ordinary Rod",
    searchable_by=["Ordinary Rod", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    condition=has_pokemon_or_basic_energy_in_discard,
    effect=ordinary_rod,
)
