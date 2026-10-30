from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import energy_stadium, energy_stadium_condition


card = StadiumCardDef(
    guid="02b0c11b-06d6-5bc7-9ee6-e920ed4bbda5",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyStadium.Name",
    display_name="Energy Stadium",
    searchable_by=["Energy Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Energy Stadium",
        game_text="Once during each player's turn (before attacking), that player may flip a coin. If heads, that player puts a basic Energy card from his or her discard pile into his or her hand.",
        activation=Activations.ONCE_PER_TURN,
        condition=energy_stadium_condition,
        effect=energy_stadium,
    ),
)
