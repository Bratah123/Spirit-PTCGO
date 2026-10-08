from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece
from spirit.game.attributes import Rarities

card = VUnionPieceCardDef(
    guid="9884302a-bc1c-584b-9fc8-48c11e28af25",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVUNION.Name",
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    collector_number=160,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MewtwoVUNION_Combined",
    piece=VUnionPiece.TOP_RIGHT,
)
