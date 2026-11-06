from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import celadon_city_gym, celadon_city_gym_condition


card = StadiumCardDef(
    guid="332ba831-6589-57d8-b8ce-a98c30f95580",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeladonCityGym.Name",
    display_name="Celadon City Gym",
    searchable_by=["Celadon City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=107,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Celadon City Gym",
        game_text="During each player's turn, that player may choose to discard an Energy card attached to 1 of his or her Pokémon with Erika in its name. If that player does so, that Pokémon is no longer Asleep, Confused, Paralyzed, or Poisoned.",
        activation=Activations.ONCE_PER_TURN,
        condition=celadon_city_gym_condition,
        effect=celadon_city_gym,
    ),
)
