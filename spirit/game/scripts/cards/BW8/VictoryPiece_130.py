from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9ee6e547-3b9d-546d-9a1c-42ad33b102e2",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryPiece.Name",
    display_name="Victory Piece",
    searchable_by=["Victory Piece", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=130,
    set_code="BW8",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
