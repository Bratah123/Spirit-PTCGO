from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a0d9688a-ccfc-5803-ac3c-59fb5d05933f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalWall.Name",
    display_name="Crystal Wall",
    searchable_by=["Crystal Wall", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=139,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
