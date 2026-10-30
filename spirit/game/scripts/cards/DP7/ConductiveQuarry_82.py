"""Conductive Quarry (DP7 #82)."""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import conductive_quarry_ability

card = StadiumCardDef(
    guid="3c15ea4d-c419-5041-a60d-a8a453342795",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ConductiveQuarry.Name",
    display_name="Conductive Quarry",
    searchable_by=["Conductive Quarry", "Stadium"],
    subtypes=["Stadium"],
    collector_number=82,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Conductive Quarry",
        game_text="Once during each player's turn, the player may flip a coin. If heads, that player searches his or her discard pile for a Lightning or Metal Energy card, shows it to the opponent, and puts it into his or her hand.",
        ability_type=AbilityTypes.POKE_BODY,
        activation=Activations.ONCE_PER_TURN,
        effect=conductive_quarry_ability(),
    ),
)
