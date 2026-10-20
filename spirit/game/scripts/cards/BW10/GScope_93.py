from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9a0c4d11-95e0-557a-9419-44218056fec8",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GScope.Name",
    display_name="G Scope",
    searchable_by=["G Scope", "Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    collector_number=93,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
