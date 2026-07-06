from spirit.game.card_effects.trainers import center_lady_playable, pokemon_center_lady
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7169f2c3-456a-50e1-aba5-f6df5f7727eb",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenterLady.Name",
    display_name="PokÃ©mon Center Lady",
    searchable_by=["Pok\u00c3\u00a9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=60,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=pokemon_center_lady,
    condition=center_lady_playable
)
