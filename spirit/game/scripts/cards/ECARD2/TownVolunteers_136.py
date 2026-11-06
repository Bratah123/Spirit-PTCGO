from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import has_pokemon_or_basic_energy_in_discard
from spirit.game.card_effects.ecard import town_volunteers


card = SupporterCardDef(
    guid="5d9ef73a-c3e2-58c5-ab14-6f9d146b056c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownVolunteers.Name",
    display_name="Town Volunteers",
    searchable_by=["Town Volunteers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    condition=has_pokemon_or_basic_energy_in_discard,
    effect=town_volunteers,
)
