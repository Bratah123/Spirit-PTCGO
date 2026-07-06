from spirit.game.card_effects.trainers import center_lady_playable, pokemon_center_lady
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a5ad23bc-7c8d-543c-b1f3-647d13ab754e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenterLady.Name",
    display_name="PokÃ©mon Center Lady",
    searchable_by=["Pok\u00c3\u00a9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="SWSH4",
    rarity=Rarities.RareUltra,
    effect=pokemon_center_lady,
    condition=center_lady_playable
)
