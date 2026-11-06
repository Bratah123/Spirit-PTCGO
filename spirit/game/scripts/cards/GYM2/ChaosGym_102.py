from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import chaos_gym_passive


card = StadiumCardDef(
    guid="f45119ca-e810-56fa-8944-a81b092242ea",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaosGym.Name",
    display_name="Chaos Gym",
    searchable_by=["Chaos Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="GYM2",
    rarity=Rarities.Rare,
    passive=chaos_gym_passive,
)
