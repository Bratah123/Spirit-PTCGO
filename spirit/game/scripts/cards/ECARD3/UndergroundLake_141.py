from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    underground_lake, underground_lake_condition,
)


card = StadiumCardDef(
    guid="cef622e7-dd42-5c7c-9221-1a22335e1ec0",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundLake.Name",
    display_name="Underground Lake",
    searchable_by=["Underground Lake", "Stadium"],
    subtypes=["Stadium"],
    collector_number=141,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Underground Lake",
        game_text="Once during each player's turn, that player may put an Omanyte or a Kabuto card from his or her discard pile onto his or her Bench. (Cards put on the Bench this way are considered Basic Pok\u00e9mon.)",
        activation=Activations.ONCE_PER_TURN,
        condition=underground_lake_condition,
        effect=underground_lake,
    ),
)
