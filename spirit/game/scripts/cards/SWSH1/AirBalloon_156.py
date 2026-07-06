from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import AirBalloonPassive

card = PokemonToolCardDef(
    guid="ef73800b-8e63-5c03-acd0-bdbf97acfe14",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AirBalloon.Name",
    display_name="Air Balloon",
    searchable_by=["Air Balloon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=156,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    passive=AirBalloonPassive(),
)
