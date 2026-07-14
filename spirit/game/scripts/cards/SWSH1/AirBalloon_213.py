from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import AirBalloonPassive

card = PokemonToolCardDef(
    guid="faf92ae5-83b9-5ffb-949b-baf09dbbacbb",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AirBalloon.Name",
    display_name="Air Balloon",
    searchable_by=["Air Balloon", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=213,
    set_code="SWSH1",
    rarity=Rarities.RareSecret,
    passive=AirBalloonPassive()
)
