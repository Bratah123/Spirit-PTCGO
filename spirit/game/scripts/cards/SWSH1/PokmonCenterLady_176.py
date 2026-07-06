from spirit.game.card_effects.trainers import center_lady_playable, pokemon_center_lady
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cb44f7b6-44f4-57ae-bf2b-aeedfe27b0db",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenterLady.Name",
    display_name="PokÃ©mon Center Lady",
    searchable_by=["Pok\u00c3\u00a9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    effect=pokemon_center_lady,
    condition=center_lady_playable
)
