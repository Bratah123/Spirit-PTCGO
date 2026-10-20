from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="72d126ec-bc95-5c63-a4ee-2094d119d97a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalEdge.Name",
    display_name="Crystal Edge",
    searchable_by=["Crystal Edge", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=138,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
