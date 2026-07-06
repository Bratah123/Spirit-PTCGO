from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import klara, has_pokemon_or_basic_energy_in_discard

card = SupporterCardDef(
    guid="83294712-7c1b-56e7-b617-570078df7df1",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Klara.Name",
    display_name="Klara",
    searchable_by=["Klara", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    condition=has_pokemon_or_basic_energy_in_discard,
    effect=klara,
)
