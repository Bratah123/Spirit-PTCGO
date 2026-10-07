from spirit.game.data_utils import VUnionPieceCardDef, VUnionPiece
from spirit.game.attributes import Rarities

card = VUnionPieceCardDef(
    guid="136fbaaa-113b-57a9-9495-e853e24cc789",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVUNION.Name",
    display_name="Mewtwo V-UNION",
    searchable_by=["Mewtwo V-UNION", "V-UNION", "MewtwoVUNION"],
    collector_number=162,
    set_code="Promo_SWSH",
    rarity=Rarities.RarePromo,
    vunion="Promo_SWSH/MewtwoVUNION_Combined",
    piece=VUnionPiece.BOTTOM_RIGHT,
)
