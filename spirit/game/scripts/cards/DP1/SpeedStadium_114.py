"""Speed Stadium (DP1 #114)."""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import speed_stadium_ability

card = StadiumCardDef(
    guid="ccc3ee1d-ce38-59cd-a7e3-cd22c9467086",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpeedStadium.Name",
    display_name="Speed Stadium",
    searchable_by=["Speed Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Speed Stadium",
        game_text="Once during each player's turn, the player may flip a coin until he or she gets tails. For each heads, that player draws a card.",
        ability_type=AbilityTypes.POKE_POWER,
        activation=Activations.ONCE_PER_TURN,
        effect=speed_stadium_ability(),
    ),
)
