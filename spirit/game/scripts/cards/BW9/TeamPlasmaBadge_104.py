from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2bd08d2b-fa60-5277-8f58-7cb39aa5cc08",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaBadge.Name",
    display_name="Team Plasma Badge",
    searchable_by=["Team Plasma Badge", "Pok\u00e9mon Tool", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "Team Plasma"],
    collector_number=104,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    # The holder is a Team Plasma Pokemon: is_team_plasma_pokemon reads the
    # grants_team_plasma flag off attached cards' definitions.
)
card.grants_team_plasma = True
