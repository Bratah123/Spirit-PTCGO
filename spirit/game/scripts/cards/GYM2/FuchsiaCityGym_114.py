from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    fuchsia_city_gym,
    fuchsia_city_gym_condition,
)


card = StadiumCardDef(
    guid="4115c0f1-efc5-53b0-b8a4-4b043ae81c7c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FuchsiaCityGym.Name",
    display_name="Fuchsia City Gym",
    searchable_by=["Fuchsia City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Fuchsia City Gym",
        game_text="Once during each player's turn (before attacking), that player may flip a coin. If heads, that player may shuffle 1 of his or her Pok\u00e9mon in play with Koga in its name and any cards attached to it into his or her deck.",
        activation=Activations.ONCE_PER_TURN,
        condition=fuchsia_city_gym_condition,
        effect=fuchsia_city_gym,
    ),
)
