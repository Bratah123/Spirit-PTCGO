from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import (
    saffron_city_gym,
    saffron_city_gym_condition,
)


card = StadiumCardDef(
    guid="43d43b08-9d0f-5e3a-b4b0-68ad948ec074",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SaffronCityGym.Name",
    display_name="Saffron City Gym",
    searchable_by=["Saffron City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=122,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Saffron City Gym",
        game_text="As often as each player like during his or her turn (before attacking), that player may return 1 basic Energy card attached to 1 of his or her Pok\u00e9mon with Sabrina in its name to his or her hand.",
        activation=Activations.UNLIMITED,
        condition=saffron_city_gym_condition,
        effect=saffron_city_gym,
    ),
)
