from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import power_plant, power_plant_condition


card = StadiumCardDef(
    guid="049dc55e-b4e4-58b7-a637-15f0c051114a",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerPlant.Name",
    display_name="Power Plant",
    searchable_by=["Power Plant", "Stadium"],
    subtypes=["Stadium"],
    collector_number=139,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Power Plant",
        game_text="Once during each of his or her turns, a player may discard a basic Energy card from his or her hand. If that player does, he or she chooses a basic Energy card from his or her discard pile, shows it to his or her opponent, and then puts it into his or her hand.",
        activation=Activations.ONCE_PER_TURN,
        condition=power_plant_condition,
        effect=power_plant,
    ),
)
