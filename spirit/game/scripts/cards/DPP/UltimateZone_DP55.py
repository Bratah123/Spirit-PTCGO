"""Ultimate Zone (DPP #DP55)."""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import ultimate_zone_ability

card = StadiumCardDef(
    guid="05e5d4af-b11f-5bdf-8166-b427833da3e4",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltimateZone.Name",
    display_name="Ultimate Zone",
    searchable_by=["Ultimate Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=55,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    ability=Ability(
        title="Ultimate Zone",
        game_text="During each player's turn, the player may move an Energy card attached to 1 of his or her Benched Pokémon to his or her Active Arceus as often as he or she likes.",
        ability_type=AbilityTypes.POKE_BODY,
        activation=Activations.UNLIMITED,
        effect=ultimate_zone_ability(),
    ),
)
